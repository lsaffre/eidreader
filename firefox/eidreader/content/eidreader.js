function EIDReaderSearch(event){
    var query = document.getElementById("EIDReaderQuery").value;
    window._content.document.location  = 
        "http://www.google.com/search?q=" + encodeURI(query);
}
