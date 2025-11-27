bot_template = """
<div class="chat-massage bot">
    <img src="https://img.icons8.com/color/48/000000/robot.png" alt="bot-icon">
    <p>{{message}}</p>
</div>
"""

user_template = """
<div class="chat-massage user">
    <img src="https://img.icons8.com/color/48/000000/user.png" alt="user-icon">
    <p>{{message}}</p>
</div>
"""

css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

/* Dark elegant background */
.stApp {
    background: #0f0f23;
    background-image: 
        radial-gradient(at 0% 0%, rgba(88, 101, 242, 0.15) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(139, 92, 246, 0.15) 0px, transparent 50%),
        radial-gradient(at 50% 50%, rgba(59, 130, 246, 0.1) 0px, transparent 50%);
    color: #e5e7eb;
}

/* Glassmorphism chat bubbles */
.chat-massage {
    padding: 1.4rem 1.6rem;
    border-radius: 1.2rem;
    margin: 1.4rem 0;
    display: flex;
    align-items: flex-start;
    gap: 1.2rem;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    animation: fadeInUp 0.5s ease-out;
    position: relative;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Bot message - Blue glass */
.bot {
    background: rgba(59, 130, 246, 0.08);
    border: 1px solid rgba(59, 130, 246, 0.2);
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.3),
        0 0 0 1px rgba(59, 130, 246, 0.1) inset,
        0 0 20px rgba(59, 130, 246, 0.1);
}

.bot:hover {
    background: rgba(59, 130, 246, 0.12);
    border-color: rgba(59, 130, 246, 0.3);
    transform: translateY(-2px);
    box-shadow: 
        0 12px 40px rgba(0, 0, 0, 0.4),
        0 0 0 1px rgba(59, 130, 246, 0.15) inset,
        0 0 30px rgba(59, 130, 246, 0.15);
}

.bot p {
    color: #e0e7ff;
    margin: 0;
    line-height: 1.7;
    font-size: 0.95rem;
    font-weight: 400;
}

.bot img {
    width: 46px;
    height: 46px;
    border-radius: 50%;
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.2), rgba(37, 99, 235, 0.3));
    padding: 8px;
    border: 1px solid rgba(59, 130, 246, 0.3);
    box-shadow: 
        0 4px 12px rgba(59, 130, 246, 0.3),
        0 0 20px rgba(59, 130, 246, 0.2);
    transition: all 0.3s ease;
}

.bot:hover img {
    transform: scale(1.1) rotate(5deg);
    box-shadow: 
        0 6px 16px rgba(59, 130, 246, 0.4),
        0 0 30px rgba(59, 130, 246, 0.3);
}

/* User message - Purple glass */
.user {
    background: rgba(139, 92, 246, 0.08);
    border: 1px solid rgba(139, 92, 246, 0.2);
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.3),
        0 0 0 1px rgba(139, 92, 246, 0.1) inset,
        0 0 20px rgba(139, 92, 246, 0.1);
    flex-direction: row-reverse;
}

.user:hover {
    background: rgba(139, 92, 246, 0.12);
    border-color: rgba(139, 92, 246, 0.3);
    transform: translateY(-2px);
    box-shadow: 
        0 12px 40px rgba(0, 0, 0, 0.4),
        0 0 0 1px rgba(139, 92, 246, 0.15) inset,
        0 0 30px rgba(139, 92, 246, 0.15);
}

.user p {
    color: #ede9fe;
    margin: 0;
    line-height: 1.7;
    font-size: 0.95rem;
    font-weight: 400;
    text-align: right;
}

.user img {
    width: 46px;
    height: 46px;
    border-radius: 50%;
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.2), rgba(124, 58, 237, 0.3));
    padding: 8px;
    border: 1px solid rgba(139, 92, 246, 0.3);
    box-shadow: 
        0 4px 12px rgba(139, 92, 246, 0.3),
        0 0 20px rgba(139, 92, 246, 0.2);
    transition: all 0.3s ease;
}

.user:hover img {
    transform: scale(1.1) rotate(-5deg);
    box-shadow: 
        0 6px 16px rgba(139, 92, 246, 0.4),
        0 0 30px rgba(139, 92, 246, 0.3);
}

/* Elegant header */
h1 {
    color: #f3f4f6 !important;
    font-weight: 700 !important;
    text-shadow: 0 0 30px rgba(59, 130, 246, 0.3);
    letter-spacing: -0.5px;
}

/* Glass input field */
.stTextInput > div > div > input {
    background: rgba(31, 41, 55, 0.5) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(75, 85, 99, 0.3) !important;
    border-radius: 0.75rem !important;
    padding: 0.85rem 1.2rem !important;
    font-size: 0.95rem !important;
    color: #f3f4f6 !important;
    transition: all 0.3s ease !important;
    box-shadow: 
        0 4px 16px rgba(0, 0, 0, 0.2),
        0 0 0 1px rgba(75, 85, 99, 0.1) inset !important;
}

.stTextInput > div > div > input:focus {
    background: rgba(31, 41, 55, 0.7) !important;
    border-color: rgba(59, 130, 246, 0.5) !important;
    box-shadow: 
        0 4px 20px rgba(0, 0, 0, 0.3),
        0 0 0 1px rgba(59, 130, 246, 0.2) inset,
        0 0 20px rgba(59, 130, 246, 0.15) !important;
}

.stTextInput > div > div > input::placeholder {
    color: rgba(156, 163, 175, 0.6) !important;
}

/* Glass button */
.stButton > button {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.15), rgba(37, 99, 235, 0.2)) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    color: #93c5fd !important;
    border: 1px solid rgba(59, 130, 246, 0.3) !important;
    border-radius: 0.75rem !important;
    padding: 0.75rem 1.8rem !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    transition: all 0.3s ease !important;
    box-shadow: 
        0 4px 16px rgba(0, 0, 0, 0.2),
        0 0 20px rgba(59, 130, 246, 0.15) !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.25), rgba(37, 99, 235, 0.3)) !important;
    border-color: rgba(59, 130, 246, 0.5) !important;
    transform: translateY(-2px) !important;
    box-shadow: 
        0 6px 24px rgba(0, 0, 0, 0.3),
        0 0 30px rgba(59, 130, 246, 0.25) !important;
    color: #bfdbfe !important;
}

.stButton > button:active {
    transform: translateY(0) !important;
}

/* Glass sidebar */
.css-1d391kg, [data-testid="stSidebar"] {
    background: rgba(17, 24, 39, 0.8) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border-right: 1px solid rgba(75, 85, 99, 0.2) !important;
}

.css-1d391kg h2, .css-1d391kg h3, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
    color: #f3f4f6 !important;
    font-weight: 600 !important;
    text-shadow: 0 0 20px rgba(139, 92, 246, 0.2);
}

/* Glass file uploader */
.stFileUploader {
    background: rgba(31, 41, 55, 0.4) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 2px dashed rgba(75, 85, 99, 0.3) !important;
    border-radius: 0.75rem !important;
    padding: 1.5rem !important;
    transition: all 0.3s ease !important;
}

.stFileUploader:hover {
    background: rgba(31, 41, 55, 0.6) !important;
    border-color: rgba(59, 130, 246, 0.4) !important;
    box-shadow: 0 0 20px rgba(59, 130, 246, 0.1);
}

/* Spinner with glow */
.stSpinner > div {
    border-top-color: #3b82f6 !important;
    filter: drop-shadow(0 0 8px rgba(59, 130, 246, 0.5));
}

/* Glass alert */
.stAlert {
    background: rgba(31, 41, 55, 0.6) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border-radius: 0.75rem !important;
    border: 1px solid rgba(75, 85, 99, 0.3) !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2) !important;
    color: #e5e7eb !important;
}

/* Elegant scrollbar */
::-webkit-scrollbar {
    width: 10px;
    height: 10px;
}

::-webkit-scrollbar-track {
    background: rgba(17, 24, 39, 0.5);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.3), rgba(139, 92, 246, 0.3));
    border-radius: 10px;
    border: 2px solid rgba(17, 24, 39, 0.5);
    box-shadow: 0 0 10px rgba(59, 130, 246, 0.2);
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.5), rgba(139, 92, 246, 0.5));
    box-shadow: 0 0 15px rgba(59, 130, 246, 0.3);
}

/* Responsive design */
@media (max-width: 768px) {
    .chat-massage {
        padding: 1.2rem 1.4rem;
        gap: 1rem;
    }
    
    .bot img, .user img {
        width: 40px;
        height: 40px;
    }
    
    .bot p, .user p {
        font-size: 0.9rem;
    }
}
</style>
"""
