
document.addEventListener("DOMContentLoaded", function () {
    const searchForm = document.getElementById("praazSearchForm");
    const toggleButton = document.getElementById("searchToggle");
    const toggleText = document.getElementById("toggleText");
    const toggleArrow = document.getElementById("toggleArrow");

    if (!searchForm || !toggleButton) return;

    // Ensure the initial state is visible
    searchForm.hidden = false;
    toggleButton.setAttribute("aria-expanded", "true");

    toggleButton.addEventListener("click", function () {
        const willHide = !searchForm.hidden;

        searchForm.hidden = willHide;

        toggleText.textContent = willHide ? "Show" : "Hide";
        toggleArrow.textContent = willHide ? "⌄" : "⌃";

        toggleButton.setAttribute(
            "aria-expanded",
            String(!willHide)
        );
    });
});
