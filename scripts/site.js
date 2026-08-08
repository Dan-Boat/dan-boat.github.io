(function () {
    // Scroll to top whenever a section tab is switched, so mobile users
    // land at the top of the new section instead of mid-scroll.
    document.querySelectorAll(".control").forEach(function (button) {
        button.addEventListener("click", function () {
            window.scrollTo({ top: 0, behavior: "instant" in window ? "auto" : "auto" });
        });
    });
})();
