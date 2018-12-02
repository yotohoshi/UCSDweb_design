//Search Control
var people = ['Jamila', 'Lakenya', 'Eulalia', 'Jules', 'Li', 'Titus', 'Marybelle', 'Loan', 'Rolland', 'Leisa', 'Noe', 'Elin', 'Bernice', 'Karly', 'Barton', 'IndiaIndiaIndiaIndiaIndiaIndiaIndiaIndia', 'Bradley', 'Rudolph', 'Cassandra', 'Vita', 'Justin', 'Edna', 'Scarlett', 'Rasheeda', 'Essie', 'Sabra', 'Eleanore', 'Christal', 'Moses', 'Rachelle', 'Shakira', 'Jona', 'Christa', 'Elaina', 'Frederica', 'Lashawn', 'Jody', 'Amanda', 'Marcellus', 'Rodney', 'Kenyatta', 'Maybell', 'Christel', 'Angle', 'Harris', 'Talia', 'Brendon', 'Reginald', 'Celestine', 'Etta'];

$.ajax({
    url: "/job_fetch_data",
    dataType: 'json',
    success: function (data) {
        console.log('Got location list!');
        locations = data.locations;
        majors = data.majors;
        degrees = data.degrees;
    }
});


function matchList(input) {
    var reg = new RegExp(input.split("").join("\\w*").replace(/\W/, ""), "i");
    var res = [];
    if (input.trim().length === 0) {
        return res;
    }
    for (var i = 0, len = people.length; i < len; i++) {
        if (people[i].match(reg)) {
            res.push(people[i]);
        }
    }
    return res;
}

function changeInput(val) {
    var autoCompleteResult = matchPeople(val);
    document.getElementById("result").innerHTML = "";
    for (var i = 0, limit = 10, len = autoCompleteResult.length; i < len && i < limit; i++) {
        document.getElementById("result").innerHTML += "<a class='list-group-item list-group-item-action' href='#' onclick='setSearch(\"" + autoCompleteResult[i] + "\")'>" + autoCompleteResult[i] + "</a>";
    }
}


function setSearch(value) {
    document.getElementById('search').value = value;
    document.getElementById("result").innerHTML = "";
}


//Step Control
$(document).ready(function () {
    $(".form-wrapper .next-button").click(function () {
        var button = $(this);
        var currentSection = button.parents(".section");
        var currentSectionIndex = currentSection.index();
        var headerSection = $('.steps li').eq(currentSectionIndex);
        currentSection.removeClass("is-active").next().addClass("is-active");
        headerSection.removeClass("is-active").next().addClass("is-active");

        $(".form-wrapper").submit(function (e) {
            e.preventDefault();
        });

        if (currentSectionIndex === 3) {
            $(document).find(".form-wrapper .section").first().addClass("is-active");
            $(document).find(".steps li").first().addClass("is-active");
        }
    });

    $(".exit-button").click(function () {
        var button = $(this);
        var currentSection = button.parents(".section");
        currentSection.removeClass("is-active").next().addClass("is-active");
        $(document).find(".form-wrapper .section").first().addClass("is-active");
        $(document).find(".steps li").first().addClass("is-active");
    })
});

