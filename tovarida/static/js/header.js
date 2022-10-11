const searchBarAnimationMs = 450;

const showSearchBar = (searchBar, context) => {
    $(context.logoBlock).hide( 'drop', { direction: 'down' }, searchBarAnimationMs, () => {
        $(searchBar).show('slide', { direction: 'right' }, searchBarAnimationMs);
    });
};


const hideSearchBar = (searchBar, context) => {
    $(searchBar).hide('slide', { direction: 'right' }, searchBarAnimationMs, () => {
        $(context.logoBlock).show( 'drop', { direction: 'up' }, searchBarAnimationMs );
    });
};


$(document).ready(function () {
    const mobileSearchBar = $('#mobile-search-bar');
    const mobileLogo = $('#mobile-logo');
    const mobileSearchToggle = $('#mobile-search-toggle');
    const searchToggleController = new BoxIconToggleController(
        mobileSearchBar, mobileSearchToggle,
        'bx-search-alt', 'bx-x',
        showSearchBar, hideSearchBar,
        {logoBlock: mobileLogo}
    );
});