// Example function 
function examples(){

    // If statement example
    if(1 < 2){
        console.log("If statement test: SUCCESS")
    }

    // For loop example
    for(let i = 0; i < 5; i++){
        console.log(i + "For loop test")
    }

    // Switch case example
    switch (2+2) {
        case 3:
          // Will not happen
          break;
        case 4:
          console.log("Switch case: SUCCESS")
          break;

      }

    // "PASS" JS Example
    try {
        // Something
        console.log("pass: SUCCESS")
    } catch(e){
        // This here can be empty
    }

    // Match example
    let compare = "test"
    compare.match("test");

    // Function example to find the higher num
    let x = 5
    let y = 2;
    function higherNum(x, y){
        let toReturn = x;
        if(y > x) toReturn = y;
        
        // See if function worked
        console.log("Highest num function: SUCCESS")

        return toReturn;
    }

    higherNum(x, y); // Calls the above function

}

examples();

/* Script example using HTML - We would likely paste the following code in index.html and we can export any functions from
here to utilize

<div>
 <button id="button">Click me</button> 

 <script> 
   var button = document.getElementById("button"); 
   button.addEventListener("click", function() { 
     console.log("Button was clicked!"); 
     
   }); 
 </script> 
</div>
 
*/