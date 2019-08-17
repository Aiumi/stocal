$(document).ready(function() {
  
  // Analyze watchlist
  
  $(".analyze").click(function() {
    console.log("hello");
    var nameArr = {}
    var i = 0
    $("#watchtest tr").each(function(index){
      name = $(this).find(".selectedCompany").text()
      name = $.trim(name)
      nameArr[i] = name;
      i = i + 1;
    });
    console.log(nameArr);
    
    $.post("/run_stocks", nameArr, function(data, status){
      document.getElementById("results").innerHTML = data;
      
      $('html, body').animate({
        scrollTop: $('#results').offset().top
        }, 'slow');
    });
  });
  
  // Search Function
  
  $(".search").keyup(function() {
    var searchTerm = $(".search").val();
    var listItem = $("#companieslist tbody").children("tr");
    var searchSplit = searchTerm.replace(/ /g, "'):containsi('");

    $.extend($.expr[":"], {
      containsi: function(elem, i, match, array) {
        return (
          (elem.textContent || elem.innerText || "")
            .toLowerCase()
            .indexOf((match[3] || "").toLowerCase()) >= 0
        );
      }
    });

    $("#companieslist tbody tr")
      .not(":containsi('" + searchSplit + "')")
      .each(function(e) {
        $(this).attr("visible", "false");
      });
    
    $("#companieslist tbody tr:containsi('" + searchSplit + "')").each(function(e) {
      if (searchSplit == "" && $(this).attr("data-hidden") == "true") {
        $(this).attr("visible", "false");
      } else {
        $(this).attr("visible", "true");
      }
    });

    var resultsCount = $('#companieslist tbody tr[visible="true"]').length;
    $(".counter").text(resultsCount + " companies");

    if (resultsCount == "0") {
      $(".no-result").show();
    } else {
      $(".no-result").hide();
    }
  });

  // Add and remove companies from watchlist 
  
  $(".remove-watchlist").click(function() {
    $("#watchlist tbody").find('input[name="record"]').each(function() {
        if ($(this).is(":checked")) {
          var parents = $(this).parents("tr");
          var parentsClone = parents.clone();
          parents.remove();
               
          $("#companieslist tbody")
            .append(parentsClone)
            .find(':checkbox:checked')
            .prop('checked', false);
        };
    });
  });

  // Find and remove selected table rows 
  $(".add-watchlist").click(function() {
    $("#companieslist tbody").find('input[name="record"]').each(function() {
        if ($(this).is(":checked")) {
          var parents = $(this).parents("tr");
          var parentsClone = parents.clone();
          parents.remove();
     
          $("#watchlist tbody")
            .append(parentsClone)
            .find(':checkbox:checked')
            .prop('checked', false);
        }
    });
  });

});


