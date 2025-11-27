bot_template = """
<div class="chat-container bot">
    <div class="bot-message">{{message}}</div>
</div>
"""

user_template = """
<div class="chat-container user">
    <div class="user-message">{{message}}</div>
</div>
"""

css = """
<style>
.chat-container {
    display: flex;
    margin-bottom: 10px;
}
.user {
    justify-content: flex-end;
}
.bot {
    justify-content: flex-start;
}   
.user-message {
    color: #000000;
    padding: 10px;
    border-radius: 10px;
    max-width: 60%;
    word-wrap: break-word;
    backdrop-filter: blur(10px);
    background-image: linear-gradient(135deg, lightgreen, lightyellow);
    
}
.bot-message {
    color: #000000;
    backdrop-filter: blur(10px);
    background-image: linear-gradient(135deg, pink, lightblue);
    padding: 10px;
    border-radius: 10px;
    max-width: 80%;
    word-wrap: break-word;
}
</style>    
"""