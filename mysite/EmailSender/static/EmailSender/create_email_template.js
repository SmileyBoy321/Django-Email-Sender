var parent_body = document.body;

/*
var create_email_btn_flex_container = document.createElement("div");
create_email_btn_flex_container.className = "flex-container";
create_email_btn_flex_container.id = "create-email-btn";
create_email_btn_flex_container.display = "flex";
create_email_btn_flex_container.flexWrap = "nowrap";
create_email_btn_flex_container.style.alignItems = "flex-end";
create_email_btn_flex_container.style.flexDirection = "column-reverse";
create_email_btn_flex_container.style.top = "0px";
create_email_btn_flex_container.style.left = "0px";
create_email_btn_flex_container.style.right = "10px";
create_email_btn_flex_container.style.bottom = "10px";
parent_body.appendChild(create_email_btn_flex_container);

var create_email_btn = document.createElement("button");
create_email_btn.id = "create-email-template";
create_email_btn.innerHTML = "Create email";

parent_body.appendChild(create_email_btn_flex_container).appendChild(create_email_btn);
*/

function show_email_template() {
    alert("clicked the button");
    var email_template = document.createElement("div");
    email_template.className = "flex-container";
    email_template.id = "email-template";
    email_template.style.display = "flex";
    email_template.style.height = "500px";
    email_template.style.width = "500px";
    parent_body.appendChild(email_template);
};
