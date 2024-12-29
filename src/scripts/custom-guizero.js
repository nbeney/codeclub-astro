function defineWidgetLinkElement(tag, widget) {
    customElements.define(
        tag,
        class extends HTMLElement {
            connectedCallback() {
                this.innerHTML = `<code><a href="/codeclub-astro/offline/lawsie.github.io/guizero/${widget.toLowerCase()}/index.html">${widget}</a></code>`;
            }
        });
}

defineWidgetLinkElement('cc-gz-app', 'App');
defineWidgetLinkElement('cc-gz-box', 'Box');
defineWidgetLinkElement('cc-gz-buttongroup', 'ButtonGroup');
defineWidgetLinkElement('cc-gz-checkbox', 'CheckBox');
defineWidgetLinkElement('cc-gz-combo', 'Combo');
defineWidgetLinkElement('cc-gz-drawing', 'Drawing');
defineWidgetLinkElement('cc-gz-listbox', 'ListBox');
defineWidgetLinkElement('cc-gz-menubar', 'MenuBar');
defineWidgetLinkElement('cc-gz-picture', 'Picture');
defineWidgetLinkElement('cc-gz-pushbutton', 'PushButton');
defineWidgetLinkElement('cc-gz-slider', 'Slider');
defineWidgetLinkElement('cc-gz-text', 'Text');
defineWidgetLinkElement('cc-gz-textbox', 'TextBox');
defineWidgetLinkElement('cc-gz-titlebox', 'TitleBox');
defineWidgetLinkElement('cc-gz-waffle', 'Waffle');
defineWidgetLinkElement('cc-gz-window', 'Window');
