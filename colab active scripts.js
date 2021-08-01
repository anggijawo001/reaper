function ConnectButton(){
    console.log("Connect pushed"); 
    document.querySelector("#top-toolbar > colab-connect-button").shadowRoot.querySelector("#connect").click() 
}
window.connectButtonInterval = setInterval(ConnectButton,60000);

function ExecutionButton(){
    var nodes = document.querySelectorAll(".cell-execution-container > colab-run-button");
    //var first = nodes[0];
    var last = nodes[nodes.length- 1];
    var execBtn = last.shadowRoot.querySelector(".cell-execution-indicator");
	var execRunning = last.shadowRoot.querySelector(".cell-execution.running");

	//If the cell is running already stop it
	if(execRunning) {
		execBtn.click();
		console.log("Stop execution", execBtn);

		setTimeout(function() {
			execBtn.click();
			console.log("Start execution", execBtn);
		}, 5000);
	} else {
		// Else start it if its not running
		execBtn.click();
		console.log("Try starting execution", execBtn);
	}
    
}

window.execButtonInterval = setInterval(ExecutionButton,1000 * 60 * 8); // every 8 min



// The clea options add to another snippet


clearInterval(window.connectButtonInterval);
clearInterval(window.execButtonInterval);