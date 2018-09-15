var currentUrl;
var urlJSON;
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
	urlJSON = JSON.stringify(currentUrl);
	uploadURL;
}
function uploadURL() {
    // ajax the JSON to the server
    $.ajax({
    type: 'POST',
    url: 'localhost:5000',
    data: urlJSON,
    success: function(data) { alert('data: ' + data); },
    contentType: "application/json",
    dataType: 'json'
});