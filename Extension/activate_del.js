var currentUrl;
chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
function(tabs){
    	currentUrl = tabs[0].url;
	postURLfunction();
	}
);
function postURLfunction(){
	//run the (url-using) function here
	chrome.extension.getBackgroundPage().console.log(currentUrl);
	document.getElementById("Title1").innerHTML = currentUrl;
}