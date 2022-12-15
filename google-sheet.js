function changeFontStyle(selectTag){
    var listValue = selectTag.options[selectTag.selectedIndex].text;
    document.getElementById("myElements").style.fontFamily = listValue;
  }

function changeFontSize(selectTag){
    var listValue = selectTag.options[selectTag.selectedIndex].text;
    document.getElementById("myElements").style.fontSize = listValue;
}
