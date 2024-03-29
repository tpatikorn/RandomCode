function inlineMathToMathML(text, integral_isunderover = true, from_isunderover = false) {
  // match inline math expression and replace with MathML
  // currently support
  // - fractions: must be in format (...)/(...). If no parentheses were given, will use +-() or whitespace to group
  // - power: e.g. x^2, (x+1)^2, (3x+1)^(2x)
  // - limit: the "approach" must be in parentheses
  // - differential: d must follow by exactly one a-z character
  // - integral: must be in the format: integral ($1, $2) where $1 and $2 are arbitrary expression. S1 will appear below and $2 above the integral sign
  // - from: the substitution vertical bar. Must be in format: from ($1, $2). Same rule as integral applies.
  // for the under/over of integral, from, and limit are generated with class="under" and class="over" by default. They do nothing, but will help you stylize it with CSS
  text = text.replace(/(?:lim|limit) *\((.+?)\)/g, "<munder><ms>lim</ms><mrow class='under'>$1</mrow></munder><ms>&nbsp;</ms>");
  while (text.indexOf("integral") >= 0) {
    if (integral_isunderover) {
      text = text.replace(/integral *\((.+?),(.+?)\)/g, "<munderover><ms>&int;</ms><mrow class='under'>$1</mrow><mrow class='over'>$2</mrow></munderover><ms>&nbsp;</ms>");
    } else {
      text = text.replace(/integral *\((.+?),(.+?)\)/g, "<msubsup><ms>&int;</ms><mrow class='under'>$1</mrow><mrow class='over'>$2</mrow></msubsup><ms>&nbsp;</ms>");
    }
  }
  while (text.indexOf("from") >= 0) {
    if (from_isunderover) {
      text = text.replace(/from *\((.+?),(.+?)\)/g, "<ms>&nbsp;</ms><munderover><ms style='font-size: 100%'>|</ms><mrow class='under'>$1</mrow><mrow class='over'>$2</mrow></munderover>");
    } else {
      text = text.replace(/from *\((.+?),(.+?)\)/g, "<ms>&nbsp;</ms><msubsup><ms style='font-size: 100%'>|</ms><mrow class='under'>$1</mrow><mrow class='over'>$2</mrow></msubsup>");
    }
  }
  // loop for nested power e.g. (x^3 + 2)^2
  while (text.indexOf("^") >= 0) {
    // has to do it this way because of how each open/close bracket has to be explicitly written in MathML
    text = text.replace(/\((.+?)\)\^\((.+?)\)/g, "<msup><mrow><mo>(</mo>$1<mo>)</mo></mrow><mrow><mo>(</mo>$2<mo>)</mo></mrow></msup>");
    text = text.replace(/\((.+?)\)\^([\w\d+\-][^+\-() ]*)/g, "<msup><mrow><mo>(</mo>$1<mo>)</mo></mrow><mrow>$2</mrow></msup>");
    text = text.replace(/([^+\-() ]+)\^\((.+?)\)/g, "<msup><mrow>$1</mrow><mrow><mo>(</mo>$2<mo>)</mo></mrow></msup>");
    text = text.replace(/([^+\-()<> ]+)\^([\w\d+\-][^+\-()<> ]*)/g, "<msup><mrow>$1</mrow><mrow>$2</mrow></msup>");
  }
  text = text.replace(/(?:([^+\-() ]+)|\((.+?)\))(?<!<)\/(?:([^+\-() ]+)|\((.+?)\))/g, "<mfrac><mrow>$1$2</mrow><mrow>$3$4</mrow></mfrac>");

  text = text.replace(/(log)_(e|\d+)/g, "<msub><ms>&nbsp;$1</ms><mn>$2</mn></msub>"); // log based numbers or e
  text = text.replace(/(log)_(\w+)/g, "<msub><ms>&nbsp;$1</ms><mi>$2</mi></msub>"); // log based variables
  text = text.replace(/(?<!<ms>)(sin|cos|tan|sec|csc|cosec|cot|log|ln)/g, "<ms>&nbsp;$1</ms>");
  text = text.replace(/->|-&gt;/g, "→");
  text = text.replace(/(?<!\w\w)(?<=[a-z])'/g, "<mo>&prime;</mo>");
  text = text.replace(/(?<!<mo>)([+\-*→(),=])(?!')/g, "<mo>$1</mo>");
  text = text.replace(/\-/g, "&minus;");
  text = text.replace(/inf|&infin;/g, "∞");
  text = text.replace(/(\d+|∞)/g, "<mn>$1</mn>");
  text = text.replace(/(?<![a-z])([a-z])(?![a-z])/g, "<mi>$1</mi>");
  text = text.replace(/(?<![a-z])d([a-z])(?![a-z])/g, "<ms>&nbsp;d</ms><mi>$1</mi>");
  return text;
}