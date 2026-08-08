(function () {
    // Scroll to top whenever a section tab is switched, so mobile users
    // land at the top of the new section instead of mid-scroll.
    document.querySelectorAll(".control").forEach(function (button) {
        button.addEventListener("click", function () {
            window.scrollTo({ top: 0, behavior: "instant" in window ? "auto" : "auto" });
        });
    });
})();

// Generic client-side pagination for archive lists (news, blog, etc).
// Markup contract:
//   <div class="paginated-list" data-page-size="8">
//     <div data-items>...one child element per item, newest first...</div>
//   </div>
//   <div class="pagination-controls">
//     <button class="pg-prev">Previous</button>
//     <span class="pg-status"></span>
//     <button class="pg-next">Next</button>
//   </div>
// Items are already sorted newest-first server-side (Liquid); this only
// slices which page is visible. No JS = every item just shows at once.
(function () {
    document.querySelectorAll(".paginated-list").forEach(function (list) {
        var itemsContainer = list.querySelector("[data-items]");
        var controls = list.nextElementSibling;
        if (!itemsContainer || !controls || !controls.classList.contains("pagination-controls")) return;

        var pageSize = parseInt(list.dataset.pageSize, 10) || 8;
        var items = Array.prototype.slice.call(itemsContainer.children);
        var totalPages = Math.max(1, Math.ceil(items.length / pageSize));
        var prevBtn = controls.querySelector(".pg-prev");
        var nextBtn = controls.querySelector(".pg-next");
        var status = controls.querySelector(".pg-status");
        var page = 0;

        function render() {
            items.forEach(function (el, i) {
                el.style.display = (i >= page * pageSize && i < (page + 1) * pageSize) ? "" : "none";
            });
            if (status) status.textContent = "Page " + (page + 1) + " of " + totalPages;
            if (prevBtn) prevBtn.disabled = page === 0;
            if (nextBtn) nextBtn.disabled = page >= totalPages - 1;
        }

        if (prevBtn) {
            prevBtn.addEventListener("click", function () {
                if (page > 0) {
                    page -= 1;
                    render();
                    list.scrollIntoView({ behavior: "smooth", block: "start" });
                }
            });
        }
        if (nextBtn) {
            nextBtn.addEventListener("click", function () {
                if (page < totalPages - 1) {
                    page += 1;
                    render();
                    list.scrollIntoView({ behavior: "smooth", block: "start" });
                }
            });
        }

        if (totalPages <= 1) {
            controls.style.display = "none";
        }
        render();
    });
})();
