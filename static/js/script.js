jQuery(document).ready(function($) {
    console.log("Content Loaded")
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
});