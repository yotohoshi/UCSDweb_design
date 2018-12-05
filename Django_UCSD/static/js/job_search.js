//Search Control
    var locations;
    var SUCCESS = true;

    $.ajax({
        url: "/job_fetch_data",
        dataType: 'json',
        success: function (data) {
            console.log('Got location list!');
            locations = data.locations;
        }
    });


    function matchList(input, data) {
        var reg = new RegExp(input.split("").join("\\w*").replace(/\W/, ""), "i");
        var res = [];
        if (input.trim().length === 0) {
            return res;
        }
        for (var i = 0, len = data.length; i < len; i++) {
            if (data[i].match(reg)) {
                res.push(data[i]);
            }
        }
        return res;
    }

    function changeInputL(val) {
        var autoCompleteResult = matchList(val, locations);
        document.getElementById("result-L").innerHTML = "";
        for (var i = 0, limit = 10, len = autoCompleteResult.length; i < len && i < limit; i++) {
            document.getElementById("result-L").innerHTML += "<a class='list-group-item list-group-item-action' href='#' onclick='setSearchL(\"" + autoCompleteResult[i] + "\")'>" + autoCompleteResult[i] + "</a>";
        }
    }

    function setSearchL(value) {
        document.getElementById('search-L').value = value;
        document.getElementById("result-L").innerHTML = "";
    }