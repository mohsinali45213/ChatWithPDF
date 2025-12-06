bot_template = """
<div class="chat-container bot">
    <div class="avatar bot-avatar">
        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z" fill="currentColor"/>
        </svg>
    </div>
    <div class="bot-message">
        <div class="message-content">{{message}}</div>
        <div class="message-glow"></div>
    </div>
</div>
"""

user_template = """
<div class="chat-container user">
    <div class="user-message">
        <div class="message-content">{{message}}</div>
        <div class="message-glow"></div>
    </div>
    <div class="avatar user-avatar">
        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" fill="currentColor"/>
        </svg>
    </div>
</div>
"""

css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&family=Rajdhani:wght@300;400;500;600&display=swap');

/* Animated Background */
.stApp {
    background: linear-gradient(135deg, #0a0a1a 0%, #1a1a3e 50%, #0d0d2b 100%);
    background-attachment: fixed;
    min-height: 100vh;
}

.stApp::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
        radial-gradient(ellipse at 20% 80%, rgba(0, 255, 255, 0.1) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 20%, rgba(138, 43, 226, 0.1) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 50%, rgba(0, 150, 255, 0.05) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
}

/* Cyber Grid Animation */
.stApp::after {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
        linear-gradient(rgba(0, 255, 255, 0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 255, 255, 0.03) 1px, transparent 1px);
    background-size: 50px 50px;
    animation: gridMove 20s linear infinite;
    pointer-events: none;
    z-index: 0;
}

@keyframes gridMove {
    0% { transform: perspective(500px) rotateX(60deg) translateY(0); }
    100% { transform: perspective(500px) rotateX(60deg) translateY(50px); }
}

/* Main Content Styling */
.main .block-container {
    position: relative;
    z-index: 1;
}

/* Chat Container */
.chat-container {
    display: flex;
    margin-bottom: 20px;
    align-items: flex-start;
    animation: messageSlide 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards;
    opacity: 0;
}

@keyframes messageSlide {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.user {
    justify-content: flex-end;
}

.bot {
    justify-content: flex-start;
}

/* Avatar Styling */
.avatar {
    width: 45px;
    height: 45px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    position: relative;
}

.bot-avatar {
    background: linear-gradient(135deg, #00d4ff, #7b2cbf);
    margin-right: 12px;
    box-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
    animation: avatarPulse 2s ease-in-out infinite;
}

.user-avatar {
    background: linear-gradient(135deg, #ff6b9d, #c44569);
    margin-left: 12px;
    box-shadow: 0 0 20px rgba(255, 107, 157, 0.5);
    animation: avatarPulse 2s ease-in-out infinite 0.5s;
}

@keyframes avatarPulse {
    0%, 100% { box-shadow: 0 0 20px rgba(0, 212, 255, 0.5); }
    50% { box-shadow: 0 0 30px rgba(0, 212, 255, 0.8), 0 0 60px rgba(0, 212, 255, 0.4); }
}

.avatar svg {
    width: 24px;
    height: 24px;
    color: white;
}

/* Message Bubbles */
.user-message, .bot-message {
    position: relative;
    padding: 16px 20px;
    border-radius: 20px;
    max-width: 70%;
    word-wrap: break-word;
    font-family: 'Rajdhani', sans-serif;
    font-size: 16px;
    font-weight: 500;
    line-height: 1.6;
    overflow: hidden;
}

.user-message {
    background: linear-gradient(135deg, rgba(255, 107, 157, 0.2), rgba(196, 69, 105, 0.3));
    border: 1px solid rgba(255, 107, 157, 0.4);
    color: #fff;
    border-radius: 20px 20px 5px 20px;
    backdrop-filter: blur(10px);
}

.bot-message {
    background: linear-gradient(135deg, rgba(0, 212, 255, 0.15), rgba(123, 44, 191, 0.2));
    border: 1px solid rgba(0, 212, 255, 0.3);
    color: #e0e0e0;
    border-radius: 20px 20px 20px 5px;
    backdrop-filter: blur(10px);
}

.message-content {
    position: relative;
    z-index: 2;
}

/* Glowing Effect */
.message-glow {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    border-radius: inherit;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.user-message:hover .message-glow {
    opacity: 1;
    box-shadow: inset 0 0 30px rgba(255, 107, 157, 0.3);
}

.bot-message:hover .message-glow {
    opacity: 1;
    box-shadow: inset 0 0 30px rgba(0, 212, 255, 0.3);
}

/* Scanning Line Animation */
.bot-message::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.2), transparent);
    animation: scan 3s ease-in-out infinite;
}

@keyframes scan {
    0% { left: -100%; }
    50% { left: 100%; }
    100% { left: 100%; }
}

/* Header Styling */
h1, .stHeader, [data-testid="stHeader"] h1 {
    font-family: 'Orbitron', monospace !important;
    background: linear-gradient(90deg, #00d4ff, #7b2cbf, #ff6b9d);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradientShift 3s ease infinite;
    text-shadow: 0 0 30px rgba(0, 212, 255, 0.5);
}

@keyframes gradientShift {
    0% { background-position: 0% center; }
    50% { background-position: 100% center; }
    100% { background-position: 0% center; }
}

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(10, 10, 26, 0.95) 0%, rgba(26, 26, 62, 0.95) 100%);
    border-right: 1px solid rgba(0, 212, 255, 0.3);
    backdrop-filter: blur(20px);
}

[data-testid="stSidebar"]::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #00d4ff, #7b2cbf, #ff6b9d);
    animation: borderGlow 2s ease-in-out infinite;
}

@keyframes borderGlow {
    0%, 100% { opacity: 0.5; }
    50% { opacity: 1; }
}

/* Input Fields */
.stTextInput > div > div > input {
    background: rgba(0, 20, 40, 0.8) !important;
    border: 1px solid rgba(0, 212, 255, 0.4) !important;
    border-radius: 12px !important;
    color: #00d4ff !important;
    font-family: 'Rajdhani', sans-serif !important;
    padding: 12px 16px !important;
    transition: all 0.3s ease !important;
}

.stTextInput > div > div > input:focus {
    border-color: #00d4ff !important;
    box-shadow: 0 0 20px rgba(0, 212, 255, 0.4) !important;
}

.stTextInput > div > div > input::placeholder {
    color: rgba(0, 212, 255, 0.5) !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, rgba(0, 212, 255, 0.2), rgba(123, 44, 191, 0.3)) !important;
    border: 1px solid rgba(0, 212, 255, 0.5) !important;
    border-radius: 12px !important;
    color: #00d4ff !important;
    font-family: 'Orbitron', monospace !important;
    font-weight: 600 !important;
    padding: 12px 24px !important;
    transition: all 0.3s ease !important;
    position: relative;
    overflow: hidden;
}

.stButton > button:hover {
    background: linear-gradient(135deg, rgba(0, 212, 255, 0.4), rgba(123, 44, 191, 0.5)) !important;
    box-shadow: 0 0 30px rgba(0, 212, 255, 0.5), 0 0 60px rgba(123, 44, 191, 0.3) !important;
    transform: translateY(-2px);
}

.stButton > button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: left 0.5s ease;
}

.stButton > button:hover::before {
    left: 100%;
}

/* File Uploader */
[data-testid="stFileUploader"] {
    border: 2px dashed rgba(0, 212, 255, 0.4) !important;
    border-radius: 16px !important;
    background: rgba(0, 20, 40, 0.5) !important;
    padding: 20px !important;
    transition: all 0.3s ease !important;
}

[data-testid="stFileUploader"]:hover {
    border-color: #00d4ff !important;
    box-shadow: 0 0 30px rgba(0, 212, 255, 0.3) !important;
}

/* Spinner */
.stSpinner > div {
    border-color: #00d4ff transparent transparent transparent !important;
}

/* Success/Warning/Error Messages */
.stSuccess {
    background: rgba(0, 255, 157, 0.1) !important;
    border: 1px solid rgba(0, 255, 157, 0.4) !important;
    border-radius: 12px !important;
}

.stWarning {
    background: rgba(255, 200, 0, 0.1) !important;
    border: 1px solid rgba(255, 200, 0, 0.4) !important;
    border-radius: 12px !important;
}

.stError {
    background: rgba(255, 50, 50, 0.1) !important;
    border: 1px solid rgba(255, 50, 50, 0.4) !important;
    border-radius: 12px !important;
}

/* Subheader */
.stSubheader, h2, h3 {
    font-family: 'Orbitron', monospace !important;
    color: #00d4ff !important;
    text-transform: uppercase;
    letter-spacing: 2px;
}

/* Labels */
label {
    font-family: 'Rajdhani', sans-serif !important;
    color: rgba(0, 212, 255, 0.8) !important;
    font-weight: 500 !important;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(0, 20, 40, 0.5);
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #00d4ff, #7b2cbf);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(180deg, #00d4ff, #ff6b9d);
}

/* Floating Particles Animation */
@keyframes float {
    0%, 100% { transform: translateY(0) rotate(0deg); opacity: 0.5; }
    50% { transform: translateY(-20px) rotate(180deg); opacity: 1; }
}

/* Text Selection */
::selection {
    background: rgba(0, 212, 255, 0.4);
    color: #fff;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .user-message, .bot-message {
        max-width: 85%;
        font-size: 14px;
    }
    
    .avatar {
        width: 35px;
        height: 35px;
    }
}
</style>    
"""