$(document).ready(function() {
  
  $(".analyze").click(function() {
    alert("hello again");
    console.log("hello");
  });

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
      $(this).attr("visible", "true");
    });

    var resultsCount = $('#companieslist tbody tr[visible="true"]').length;
    $(".counter").text(resultsCount + " companies(s)");

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


