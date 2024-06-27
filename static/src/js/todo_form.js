/** @odoo-module **/

import {registry} from "@web/core/registry";
import {CharField, charField} from "@web/views/fields/char/char_field";
const {useEffect} = owl;


export class EnterConfirm extends CharField {

    setup() {
        super.setup(...arguments);
        const input = this.input || this.textareaRef;
        useEffect(() => {
            if (input.el) {
                input.el.addEventListener("keydown", this.onKeydown.bind(this));
                return () => {
                    input.el.removeEventListener("keydown", this.onKeydown.bind(this));
                };
            }
        });
    }

    async onKeydown(ev) {
        if(ev.key === 'Enter'){
            document.getElementsByName("add_task")[0].click();
        }
    }
}


export const enterConfirm = {
    ...charField,
    component: EnterConfirm,
};

registry.category("fields").add("enter_confirm", enterConfirm);
