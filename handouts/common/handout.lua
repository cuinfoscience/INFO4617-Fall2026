--[[
handout.lua -- turn a handout .qmd into LaTeX for handout.cls.

The same .qmd also becomes a notebook (make_notebook.py), so the source
stays plain markdown. This filter maps it onto the class when rendering
a PDF:

  ## Step 1 --- Title          a frame with a gold title bar
  ```python ... ```            a code cell (code environment)
  ```{.out} ... ```            an output cell (out environment); with
                               markers="4:1 5:2" it becomes a table of the
                               lines with marker n beside line k
  ::: {.out} pipe table :::    a DataFrame output (dfout environment)
  a pipe table                 a small booktabs table
  :::: {.columns align="T"}    columns; ::: {.column width="60%"}
  ::: {.alertblock title=""}   also .block and .exampleblock
  ::: {.legend} list :::       "① text" items as a two-column table
  ::: {.caption} :::           a small, ragged-right figure caption
  ::: {.pdf-only} :::          kept here, dropped from the notebook
  ::: {.notebook-only} :::     dropped here, kept in the notebook
  ![](img/x.png){fig-alt=""}   the figure, at the column width; x.pdf is
                               used instead when it exists (vector)
  `inline code`                \texttt, or \breakcode for long names

Markers are plain characters ① to ⑨; the class prints them as markers.
--]]

if not FORMAT:match("latex") then
  return {}
end

local function raw(s) return pandoc.RawBlock("latex", s) end
local function rawi(s) return pandoc.RawInline("latex", s) end

-- blocks between two raw LaTeX lines
local function wrap(before, blocks, after)
  local out = pandoc.Blocks({raw(before)})
  out:extend(blocks)
  out:insert(raw(after))
  return out
end

-- the directory of the .qmd, to look for a vector .pdf next to a .png
local input_dir = "."
if PANDOC_STATE and PANDOC_STATE.input_files and #PANDOC_STATE.input_files > 0 then
  input_dir = pandoc.path.directory(PANDOC_STATE.input_files[1])
end
local function file_exists(path)
  local f = io.open(pandoc.path.join({input_dir, path}), "r")
  if f then f:close() return true end
  return false
end

-- escape one string for \texttt{}: every special character, and "-" so
-- that "--" does not become a dash
local tt_map = {
  ["\\"] = "\\textbackslash{}", ["{"] = "\\{", ["}"] = "\\}",
  ["#"] = "\\#", ["$"] = "\\$", ["%"] = "\\%", ["&"] = "\\&",
  ["_"] = "\\_", ["^"] = "\\textasciicircum{}", ["~"] = "\\textasciitilde{}",
  ["-"] = "-{}",
}
local function tt_escape(s)
  return (s:gsub("[\\{}#$%%&_%^~%-]", tt_map))
end

-- inlines -> LaTeX (element filters below have already run on them)
local function inlines_latex(inlines)
  return pandoc.write(pandoc.Pandoc({pandoc.Plain(inlines)}), "latex"):gsub("%s+$", "")
end
local function blocks_latex(blocks)
  return pandoc.write(pandoc.Pandoc(blocks), "latex"):gsub("%s+$", "")
end

function Code(el)
  local t = el.text
  if t:match("^[%w_%.%-]+$") and (t:find("%-%-") or t:find("__")) then
    return rawi("\\breakcode{" .. t .. "}")
  end
  return rawi("\\texttt{" .. tt_escape(t) .. "}")
end

-- \ol|...| needs a delimiter that the line does not contain
local function ol(line)
  for _, d in ipairs({"|", "!", "+", "@", "/"}) do
    if not line:find(d, 1, true) then
      return "\\ol" .. d .. line .. d
    end
  end
  error("no delimiter for output line: " .. line)
end

function CodeBlock(el)
  if el.classes:includes("out") then
    local spec = el.attributes["markers"]
    if not spec then
      return raw("\\begin{out}\n" .. el.text .. "\n\\end{out}")
    end
    local marks = {}
    for k, n in spec:gmatch("(%d+):(%d+)") do marks[tonumber(k)] = n end
    local rows, i = {}, 0
    for line in (el.text .. "\n"):gmatch("(.-)\n") do
      i = i + 1
      local m = marks[i] and ("\\marker{" .. marks[i] .. "}") or ""
      rows[#rows + 1] = ol(line) .. " & " .. m .. "\\\\"
    end
    return raw("\\begin{dfout}{@{}l@{\\hspace{14pt}}c@{}}\n"
               .. table.concat(rows, "\n") .. "\n\\end{dfout}")
  end
  -- everything else is code the reader types
  return raw("\\begin{code}\n" .. el.text .. "\n\\end{code}")
end

-- a pipe table as tabular rows; header cells in bold typewriter
local function table_rows(tbl, index_bold)
  local simple = pandoc.utils.to_simple_table(tbl)
  local cols = {}
  for _, a in ipairs(simple.aligns) do
    cols[#cols + 1] = (a == "AlignRight") and "r" or "l"
  end
  local lines = {}
  local head = {}
  for _, cell in ipairs(simple.headers) do
    local text = pandoc.utils.stringify(cell)
    head[#head + 1] = (text == "") and "" or ("\\hd{" .. tt_escape(text) .. "}")
  end
  lines[#lines + 1] = table.concat(head, " & ") .. "\\\\"
  lines[#lines + 1] = "\\midrule"
  for _, row in ipairs(simple.rows) do
    local cells = {}
    for j, cell in ipairs(row) do
      local text = blocks_latex(cell)
      if j == 1 and index_bold then text = "\\textbf{" .. pandoc.utils.stringify(cell) .. "}" end
      cells[#cells + 1] = text
    end
    lines[#lines + 1] = table.concat(cells, " & ") .. "\\\\"
  end
  return "@{}" .. table.concat(cols) .. "@{}", lines
end

function Table(tbl)
  local spec, lines = table_rows(tbl, false)
  return raw("\\par\\smallskip{\\fontsize{7.6}{9.2}\\selectfont\\setlength{\\tabcolsep}{3.5pt}%\n"
             .. "\\begin{tabular}{" .. spec .. "}\n\\toprule\n"
             .. table.concat(lines, "\n") .. "\n\\bottomrule\n\\end{tabular}\\par}")
end

-- a figure: a paragraph that holds only an image
function Para(el)
  if #el.content == 1 and el.content[1].t == "Image" then
    local img = el.content[1]
    local src = img.src
    local pdf = src:gsub("%.png$", ".pdf")
    if pdf ~= src and file_exists(pdf) then src = pdf end
    local alt = img.attributes["fig-alt"] or pandoc.utils.stringify(img.caption)
    return raw("\\BeginAccSupp{method=pdfstringdef,Alt={" .. alt .. "}}%\n"
               .. "\\includegraphics[width=\\linewidth]{" .. src .. "}%\n"
               .. "\\EndAccSupp{}\\par")
  end
end

local function width_fraction(w)
  local pct = w and w:match("^([%d%.]+)%%$")
  if pct then return string.format("%.4g", tonumber(pct) / 100) end
  return "0.5"
end

function Div(el)
  local c = el.classes
  if c:includes("notebook-only") then
    return {}
  elseif c:includes("pdf-only") then
    return el.content
  elseif c:includes("columns") then
    local align = el.attributes["align"]
    local opt = align and ("[" .. align .. "]") or ""
    return wrap("\\begin{columns}" .. opt, el.content, "\\end{columns}")
  elseif c:includes("column") then
    return wrap("\\begin{column}{" .. width_fraction(el.attributes["width"]) .. "\\textwidth}",
                el.content, "\\end{column}")
  elseif c:includes("alertblock") or c:includes("block") or c:includes("exampleblock") then
    local env = c:includes("alertblock") and "alertblock"
             or c:includes("exampleblock") and "exampleblock" or "block"
    local title = el.attributes["title"] or ""
    return wrap("\\begin{" .. env .. "}{" .. title .. "}", el.content,
                "\\end{" .. env .. "}")
  elseif c:includes("caption") then
    return wrap("{\\small\\raggedright", el.content, "\\par}")
  elseif c:includes("out") then
    -- a DataFrame: the (already converted) table is replaced by dfout
    local out = {}
    for _, b in ipairs(el.content) do
      if b.t == "Table" then
        local spec, lines = table_rows(b, true)
        out[#out + 1] = raw("\\begin{dfout}{" .. spec .. "}\n"
                            .. table.concat(lines, "\n") .. "\n\\end{dfout}")
      else
        out[#out + 1] = b
      end
    end
    return out
  elseif c:includes("legend") then
    local rows = {}
    for _, list in ipairs(el.content) do
      if list.t == "BulletList" then
        for _, item in ipairs(list.content) do
          local text = blocks_latex(item)
          local mark, rest = text:match("^(%S+)%s+(.*)$")
          rows[#rows + 1] = mark .. " & " .. rest .. "\\\\[2pt]"
        end
      end
    end
    return raw("{\\small\\begin{tabular}{@{}l@{\\hspace{4pt}}"
               .. ">{\\raggedright\\arraybackslash}p{0.82\\linewidth}@{}}\n"
               .. table.concat(rows, "\n") .. "\n\\end{tabular}\\par}")
  end
end

-- ## headings start frames: \begin{frame}{title} ... \end{frame}
local function frames(doc)
  local out, open = {}, false
  for _, b in ipairs(doc.blocks) do
    if b.t == "Header" and b.level == 2 then
      if open then out[#out + 1] = raw("\\end{frame}") end
      out[#out + 1] = raw("\\begin{frame}{" .. inlines_latex(b.content) .. "}")
      open = true
    else
      out[#out + 1] = b
    end
  end
  if open then out[#out + 1] = raw("\\end{frame}") end
  doc.blocks = out
  return doc
end

-- Passes: inline code first (so later passes see its LaTeX), then divs
-- (so a table inside ::: {.out} is still a Table when Div() sees it), then
-- code blocks, tables, and figures, and last the frames.
return {
  { Code = Code },
  { Div = Div },
  { CodeBlock = CodeBlock, Table = Table, Para = Para },
  { Pandoc = frames },
}
