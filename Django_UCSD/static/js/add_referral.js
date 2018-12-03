 //Search Control
    var majors, locations, degrees, companies;
    var SUCCESS = false;

    $.ajax({
        url: "/job_fetch_data",
        dataType: 'json',
        success: function (data) {
            console.log('Got location list!');
            locations = data.locations;
            majors = data.majors;
            degrees = data.degrees;
            companies = data.companies;
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

    function changeInputM(val) {
        var autoCompleteResult = matchList(val, majors);
        document.getElementById("result-M").innerHTML = "";
        for (var i = 0, limit = 10, len = autoCompleteResult.length; i < len && i < limit; i++) {
            document.getElementById("result-M").innerHTML += "<a class='list-group-item list-group-item-action' href='#' onclick='setSearchM(\"" + autoCompleteResult[i] + "\")'>" + autoCompleteResult[i] + "</a>";
        }
    }

    function changeInputD(val) {
        var autoCompleteResult = matchList(val, degrees);
        document.getElementById("result-D").innerHTML = "";
        for (var i = 0, limit = 10, len = autoCompleteResult.length; i < len && i < limit; i++) {
            document.getElementById("result-D").innerHTML += "<a class='list-group-item list-group-item-action' href='#' onclick='setSearchD(\"" + autoCompleteResult[i] + "\")'>" + autoCompleteResult[i] + "</a>";
        }
    }

    function changeInputC(val) {
        var autoCompleteResult = matchList(val, companies);
        document.getElementById("result-C").innerHTML = "";
        for (var i = 0, limit = 10, len = autoCompleteResult.length; i < len && i < limit; i++) {
            document.getElementById("result-C").innerHTML += "<a class='list-group-item list-group-item-action' href='#' onclick='setSearchC(\"" + autoCompleteResult[i] + "\")'>" + autoCompleteResult[i] + "</a>";
        }
    }

    function setSearchL(value) {
        document.getElementById('search-L').value = value;
        document.getElementById("result-L").innerHTML = "";
    }

    function setSearchM(value) {
        document.getElementById('search-M').value = value;
        document.getElementById("result-M").innerHTML = "";
    }

    function setSearchD(value) {
        document.getElementById('search-D').value = value;
        document.getElementById("result-D").innerHTML = "";
    }

    function setSearchC(value) {
        document.getElementById('search-C').value = value;
        document.getElementById("result-C").innerHTML = "";
    }

    //Step Control
    $(document).ready(function () {
        $(".form-wrapper .next-button").click(function () {
            var button = $(this);
            var currentSection = button.parents(".section");
            var currentSectionIndex = currentSection.index();
            var headerSection = $('.steps li').eq(currentSectionIndex);
            if (currentSectionIndex !== 2) {
                currentSection.removeClass("is-active").next().addClass("is-active");
                headerSection.removeClass("is-active").next().addClass("is-active");
            }

            $(".form-wrapper").submit(function (e) {
                e.preventDefault();
            });
            if (currentSectionIndex === 2) {

                submit();
                if (SUCCESS) {
                    currentSection.removeClass("is-active").next().addClass("is-active");
                    headerSection.removeClass("is-active").next().addClass("is-active");
                } else {
                    alert("Oops, something went wrong, please try again!")
                }
            }
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

    function submit() {
        alert('hello');
        //var he = document.forms["form"]["he"].value;
        var position = document.getElementById('position').value;
        var company = document.getElementById('search-C').value;
        var major = document.getElementById('search-M').value;
        var degree = document.getElementById('search-D').value;
        var location = document.getElementById('search-L').value;
        var S = document.getElementById('S').value;
        var E = document.getElementById('E').value;
        var H = document.getElementById('H').value;
        var EM = document.getElementById('EM').value;
        var A = document.getElementById('A').value;
        var AR = document.getElementById('AR').value;
        var B = document.getElementById('B').value;
        var M = document.getElementById('M').value;
        var AC = document.getElementById('AC').value;
        var PHY = document.getElementById('PHY').value;
        var COMM = document.getElementById('COMM').value;
        var C = document.getElementById('C').value;
        var SC = document.getElementById('SC').value;
        var MUS = document.getElementById('MUS').value;
        var BIO = document.getElementById('BIO').value;
        var BE = document.getElementById('BE').value;
        var CHEM = document.getElementById('CHEM').value;
        var ELE = document.getElementById('ELE').value;
        var BC = document.getElementById('BC').value;
        var L = document.getElementById('L').value;
        var description = document.getElementById("_description").value;
        var resume_required = document.getElementById('resume_required').value;
        var referral_description = document.getElementById('referral_description').value;
        //alert(S);
        $.ajax({
            url: "/add_referral",
            data: {
                //csrfmiddlewaretoken: {% csrf_token %},
                'position': position,
                'company': company,
                'major': major,
                'degree': degree,
                'location': location,
                'S': S,
                'E': E,
                'H': H,
                'EM': EM,
                'A': A,
                'AR': AR,
                'B': B,
                'M': M,
                'AC': AC,
                'PHY': PHY,
                'COMM': COMM,
                'C': C,
                'SC': SC,
                'BIO': BIO,
                'BE': BE,
                'MUS': MUS,
                'CHEM': CHEM,
                'ELE': ELE,
                'BC': BC,
                'L': L,
                'description': description,
                'resume_required': resume_required,
                'referral_description': referral_description,
            },
            dataType: 'json',
            success: function (data) {
                if (data.successful) {
                    SUCCESS = true;
                }
            },

        });
    }