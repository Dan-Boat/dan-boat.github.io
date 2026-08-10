(function () {
    // Scroll to top whenever a section tab is switched, so mobile users
    // land at the top of the new section instead of mid-scroll.
    document.querySelectorAll(".control").forEach(function (button) {
        button.addEventListener("click", function () {
            window.scrollTo({ top: 0, behavior: "instant" in window ? "auto" : "auto" });
        });
    });
})();

// Generic client-side pagination for archive lists (news, blog, etc),
// optionally combined with theme filtering (news only, for now).
// Markup contract:
//   <div class="paginated-list" id="..." data-page-size="8">
//     <div data-items data-category-attr>...one child element per item, newest first...</div>
//   </div>
//   <div class="pagination-controls">
//     <button class="pg-prev">Previous</button>
//     <span class="pg-status"></span>
//     <button class="pg-next">Next</button>
//   </div>
// Items are already sorted newest-first server-side (Liquid); this only
// slices which page (and, if filtered, which category) is visible. No JS =
// every item just shows at once.
(function () {
    document.querySelectorAll(".paginated-list").forEach(function (list) {
        var itemsContainer = list.querySelector("[data-items]");
        var controls = list.nextElementSibling;
        if (!itemsContainer || !controls || !controls.classList.contains("pagination-controls")) return;

        var pageSize = parseInt(list.dataset.pageSize, 10) || 8;
        var allItems = Array.prototype.slice.call(itemsContainer.children);
        var filtered = allItems;
        var prevBtn = controls.querySelector(".pg-prev");
        var nextBtn = controls.querySelector(".pg-next");
        var status = controls.querySelector(".pg-status");
        var page = 0;

        function totalPages() {
            return Math.max(1, Math.ceil(filtered.length / pageSize));
        }

        function render() {
            var pages = totalPages();
            allItems.forEach(function (el) { el.style.display = "none"; });
            filtered
                .slice(page * pageSize, (page + 1) * pageSize)
                .forEach(function (el) { el.style.display = ""; });
            if (status) status.textContent = "Page " + (page + 1) + " of " + pages;
            if (prevBtn) prevBtn.disabled = page === 0;
            if (nextBtn) nextBtn.disabled = page >= pages - 1;
            controls.style.display = pages <= 1 ? "none" : "";
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
                if (page < totalPages() - 1) {
                    page += 1;
                    render();
                    list.scrollIntoView({ behavior: "smooth", block: "start" });
                }
            });
        }

        // Exposed so a filter nav (below) can narrow the item set.
        list.applyFilter = function (category) {
            filtered = category === "all"
                ? allItems
                : allItems.filter(function (el) { return el.dataset.category === category; });
            page = 0;
            render();
        };

        render();
    });
})();

// Theme filter sidebar on /news/ — clicking a theme narrows the paginated
// list above via list.applyFilter (set up by the pagination block above).
(function () {
    document.querySelectorAll(".filter-list").forEach(function (navList) {
        var targetSelector = navList.dataset.target;
        var target = targetSelector && document.querySelector(targetSelector);
        if (!target || typeof target.applyFilter !== "function") return;

        var items = navList.querySelectorAll(".filter-item");
        items.forEach(function (btn) {
            btn.addEventListener("click", function () {
                items.forEach(function (b) { b.classList.remove("active"); });
                btn.classList.add("active");
                target.applyFilter(btn.dataset.filter);
            });
        });
    });
})();
