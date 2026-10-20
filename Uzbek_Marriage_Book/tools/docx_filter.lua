-- Map Arabic divs to a dedicated right-to-left paragraph style in DOCX.
function Div(el)
  if el.classes:includes("arabic") then
    el.attributes["custom-style"] = "Arabic Quote"
    return el
  end
end
