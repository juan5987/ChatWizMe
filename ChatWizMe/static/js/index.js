const container = document.querySelector('.chatbox_container');

window.addEventListener('DOMContentLoaded', () => {
    container.scrollTop = container.scrollHeight
    // const chatbox_form = document.querySelector('.form');
    // const chatbox_container = document.querySelector('.chatbox_container');

    // chatbox_form.addEventListener("submit", (e) => {
    //     e.preventDefault();
    //     const user_input = chatbox_form.querySelector('#id_text_msg');

    //     // création de la div container du message
    //     const div = document.createElement("div")
    //     div.classList.add("chatbox_message_container_left");
    //     chatbox_container.appendChild(div);

    //     //création de la span du message
    //     const span = document.createElement("span")
    //     span.classList.add("chatbox_message");
    //     span.classList.add("user-msg");
    //     div.appendChild(span)
    //     span.innerText = user_input.value

    //     //création de la span de l'heure d'envoi
    //     const time = document.createElement("span");
    //     time.classList.add("chatbox_message_time");
    //     span.appendChild(time);
    //     const date = new Date()
    //     let hour = date.getHours();
    //     let minutes = date.getMinutes();
    //     if (minutes < 10)
    //         time.innerText = hour + ":0" + minutes
    //     else
    //     time.innerText = hour + ":" + minutes

    //     user_input.value = ""
    // })
});