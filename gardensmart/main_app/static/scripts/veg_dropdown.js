//Add event listener for the dropdown menu
let vegSelectEl = document.getElementById("veg-seed");

console.log("Script works!");

vegSelectEl.addEventListener("change", function () {
  console.log("Event listener works!");
  console.log(vegSelectEl.value);
  //let test = "{{seeds}}";

  let description = vegSelectEl.description;
  let cost = vegSelectEl.cost;

  console.log(`Description is : ${description} and cost is ${cost}`);
  //console.log(`Seeds passed parameter is : ${seeds}`);
});
