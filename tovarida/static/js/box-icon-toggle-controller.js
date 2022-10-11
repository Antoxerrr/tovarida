class BoxIconToggleController {
    constructor(targetElement, toggleElement, bxShowClass, bxHideClass, showFunc, hideFunc, context) {
        this._targetElement = targetElement;
        this._toggleElement = toggleElement;
        this._bxShowClass = bxShowClass;
        this._bxHideClass = bxHideClass;
        this._showFunc = showFunc;
        this._hideFunc = hideFunc;
        this._context = context;

        this._initEvents();
    }

    _initEvents() {
        $(this._toggleElement).click(() => this._handleClick());
    }

    _handleClick() {
        let collapsed = $(this._targetElement).css('display') === 'none';
        collapsed ? this._show() : this._hide();
    }

    _show() {
        this._showFunc ?
            this._showFunc(this._targetElement, this._context) :
            $(this._targetElement).show();
        let toggleIcon = this._toggleElement.find('.bx');
        toggleIcon.removeClass(this._bxShowClass);
        toggleIcon.addClass(this._bxHideClass);
    }

    _hide() {
        this._hideFunc ?
            this._hideFunc(this._targetElement, this._context) :
            $(this._targetElement).hide();
        let toggleIcon = this._toggleElement.find('.bx');
        toggleIcon.removeClass(this._bxHideClass);
        toggleIcon.addClass(this._bxShowClass);
    }
}