# # # Requires: pip install streamlit openai
# # import streamlit as st
# # import openai
# # from openai import OpenAI
# # import os

# # # # ----- AUTH -----
# # # if "authenticated" not in st.session_state:
# # #     st.session_state.authenticated = False

# # # if not st.session_state.authenticated:
# # #     st.title("🔐 Acceso restringido")
# # #     password = st.text_input("Introduce la contraseña:", type="password")
# # #     if password == st.secrets["auth"]["password"]:
# # #         st.session_state.authenticated = True
# # #         st.success("✅ Acceso concedido")
# # #         st.rerun()
# # #     elif password:
# # #         st.error("❌ Contraseña incorrecta")
# # #     st.stop()

# # # ----- AUTH -----
# # if "authenticated" not in st.session_state:
# #     st.session_state.authenticated = False

# # if not st.session_state.authenticated:
# #     st.set_page_config(page_title="🔐 Acceso restringido")
# #     st.title("🔐 Acceso restringido")
# #     password = st.text_input("Introduce la contraseña:", type="password")
# #     if password == st.secrets["auth"]["password"]:
# #         st.session_state.authenticated = True
# #         st.success("✅ Acceso concedido")
# #         st.rerun()
# #     elif password:
# #         st.error("❌ Contraseña incorrecta")
# #     st.stop()  # Ensures no other app content is shown

# # Requires: pip install streamlit openai
# import streamlit as st
# import openai
# from openai import OpenAI
# import os



# # ----- CONFIG -----
# MODEL = "gpt-4o"
# MAX_TOKENS = 500
# PRICING = {
#     "gpt-4o": {"input_per_million": 0.01, "output_per_million": 0.03},
# }

# # ----- INIT -----
# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         {"role": "system", "content": "Eres un asistente curioso que hace preguntas de seguimiento interesantes basadas en las respuestas del usuario. Habla únicamente en español."},
#         {"role": "assistant", "content": "¿Cuál es tu comida favorita?"}
#     ]

# if "rounds" not in st.session_state:
#     st.session_state.rounds = 0

# # ----- SETUP -----
# st.set_page_config(page_title="Asistente en Español", page_icon="🗣️")
# st.title("🗣️ Chatbot en Español con Corrección")

# # api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
# # if not api_key:
# #     api_key = st.text_input("🔑 Introduce tu clave de API de OpenAI", type="password")
# # if not api_key:
# #     st.warning("Se necesita la clave API para continuar.")
# #     st.stop()

# # client = OpenAI(api_key=api_key)

# # ----- API KEY SETUP -----
# if "api_key" not in st.session_state:
#     st.session_state.api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

# if not st.session_state.api_key:
#     key_input = st.text_input("🔑 Introduce tu clave de API de OpenAI", type="password")
#     if key_input:
#         st.session_state.api_key = key_input
#         st.rerun()

# if not st.session_state.api_key:
#     st.warning("Se necesita la clave API para continuar.")
#     st.stop()

# client = OpenAI(api_key=st.session_state.api_key)




# # ----- PAGE CONFIG (only once, at the top!) -----
# st.set_page_config(page_title="🗣️ Chatbot en Español con Corrección", page_icon="🗣️")

# # ----- AUTH -----
# if "authenticated" not in st.session_state:
#     st.session_state.authenticated = False

# if not st.session_state.authenticated:
#     st.title("🔐 Acceso restringido")
#     password = st.text_input("Introduce la contraseña:", type="password")
#     if password == st.secrets["auth"]["password"]:
#         st.session_state.authenticated = True
#         st.success("✅ Acceso concedido")
#         st.rerun()
#     elif password:
#         st.error("❌ Contraseña incorrecta")
#     st.stop()







# # ----- CHAT DISPLAY -----
# for msg in st.session_state.messages[1:]:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # ----- USER INPUT -----
# user_input = st.chat_input("Escribe tu respuesta (o 'exit' para salir)...")
# if user_input:
#     if user_input.lower() in {"exit", "salir"}:
#         st.write("👋 ¡Gracias por chatear!")
#         st.stop()

#     # Display user message
#     st.chat_message("user").markdown(user_input)
#     st.session_state.messages.append({"role": "user", "content": user_input})

#     # Language detection for feedback
#     lang_resp = client.chat.completions.create(
#         model=MODEL,
#         messages=[
#             {"role": "system", "content": "Identify if the following text is in English or Spanish. Respond with only 'English' or 'Spanish'."},
#             {"role": "user", "content": user_input},
#         ],
#         max_tokens=10,
#     )
#     lang = lang_resp.choices[0].message.content.strip().lower()

#     if lang == "english":
#         system_msg = "You are a helpful English spelling tutor. If there are spelling mistakes in the user's sentence, point them out and show the corrected version. If it is already correct, say 'No spelling issues.'"
#     elif lang == "spanish":
#         system_msg = "Eres un corrector de español. Si hay errores gramaticales o de ortografía en la oración del usuario, corrígelos y explica brevemente el error. Si todo está bien, di 'Sin errores.'"
#     else:
#         system_msg = None

#     if system_msg:
#         correction = client.chat.completions.create(
#             model=MODEL,
#             messages=[
#                 {"role": "system", "content": system_msg},
#                 {"role": "user", "content": user_input},
#             ],
#             max_tokens=100,
#         ).choices[0].message.content.strip()
#         if correction.lower() not in {"no spelling issues.", "sin errores."}:
#             st.info(f"🔍 **Corrección sugerida:** {correction}")

#     # GPT response
#     with st.spinner("Pensando..."):
#         response = client.chat.completions.create(
#             model=MODEL,
#             messages=st.session_state.messages,
#             max_tokens=MAX_TOKENS,
#         )

#     bot_reply = response.choices[0].message.content.strip()
#     st.chat_message("assistant").markdown(bot_reply)
#     st.session_state.messages.append({"role": "assistant", "content": bot_reply})

#     # Cost breakdown
#     pt = getattr(response.usage, "prompt_tokens", 0)
#     ct = getattr(response.usage, "completion_tokens", 0)
#     total_tokens = pt + ct
#     cost = (pt / 1_000_000) * PRICING[MODEL]["input_per_million"] + (ct / 1_000_000) * PRICING[MODEL]["output_per_million"]
#     st.caption(f"🧮 Tokens: {total_tokens} | Cost: ${cost:.8f}")

#     st.session_state.rounds += 1


























# Requires: pip install streamlit openai
import os
import streamlit as st
import openai
from openai import OpenAI

# ──────────────────────────────────────────────────────────────────────────────
# PAGE + APP CONFIG (call once)
# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(page_title="🗣️ Chatbot en Español con Corrección", page_icon="🗣️")
st.title("🗣️ Chatbot en Español con Corrección")

MODEL = "gpt-4o"
MAX_TOKENS = 500
PRICING = {"gpt-4o": {"input_per_million": 0.01, "output_per_million": 0.03}}

# ──────────────────────────────────────────────────────────────────────────────
# AUTH GATE (optional password)
# ──────────────────────────────────────────────────────────────────────────────
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.subheader("🔐 Acceso restringido")
    password = st.text_input("Introduce la contraseña:", type="password")
    try:
        app_pw = st.secrets["auth"]["password"]
    except Exception:
        app_pw = None
    if app_pw and password == app_pw:
        st.session_state.authenticated = True
        st.success("✅ Acceso concedido")
        st.rerun()
    elif password:
        st.error("❌ Contraseña incorrecta")
    st.stop()

# ──────────────────────────────────────────────────────────────────────────────
# OPENAI CREDENTIALS
# ──────────────────────────────────────────────────────────────────────────────
if "api_key" not in st.session_state:
    # Prefer Streamlit secrets, then env var; allow user input as fallback
    st.session_state.api_key = (
        st.secrets.get("OPENAI_API_KEY", None) or os.getenv("OPENAI_API_KEY")
    )

org_id = st.secrets.get("OPENAI_ORG_ID", None) if "OPENAI_ORG_ID" in st.secrets else os.getenv("OPENAI_ORG_ID")
proj_id = st.secrets.get("OPENAI_PROJECT_ID", None) if "OPENAI_PROJECT_ID" in st.secrets else os.getenv("OPENAI_PROJECT_ID")

if not st.session_state.api_key:
    key_input = st.text_input("🔑 Introduce tu clave de API de OpenAI", type="password")
    if key_input:
        st.session_state.api_key = key_input
        st.rerun()

if not st.session_state.api_key:
    st.warning("Se necesita la clave API para continuar.")
    st.stop()

# Build client; include org/project if provided
client_kwargs = {"api_key": st.session_state.api_key}
if org_id:
    client_kwargs["organization"] = org_id
if proj_id:
    client_kwargs["project"] = proj_id
client = OpenAI(**client_kwargs)

# ──────────────────────────────────────────────────────────────────────────────
# CHAT STATE
# ──────────────────────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Eres un asistente curioso que hace preguntas de seguimiento interesantes basadas en las respuestas del usuario. Habla únicamente en español."},
        {"role": "assistant", "content": "¿Cuál es tu comida favorita?"},
    ]

if "rounds" not in st.session_state:
    st.session_state.rounds = 0

# ──────────────────────────────────────────────────────────────────────────────
# DISPLAY HISTORY (skip system)
# ──────────────────────────────────────────────────────────────────────────────
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ──────────────────────────────────────────────────────────────────────────────
# USER INPUT
# ──────────────────────────────────────────────────────────────────────────────
user_input = st.chat_input("Escribe tu respuesta (o 'exit' para salir)...")
if user_input:
    if user_input.lower().strip() in {"exit", "salir"}:
        st.write("👋 ¡Gracias por chatear!")
        st.stop()

    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # ── Language detection for feedback ───────────────────────────────────────
    lang = "spanish"
    try:
        lang_resp = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "Identify if the following text is in English or Spanish. Respond with only 'English' or 'Spanish'."},
                {"role": "user", "content": user_input},
            ],
            max_tokens=10,
        )
        lang = lang_resp.choices[0].message.content.strip().lower()
    except openai.AuthenticationError:
        st.error("❌ Error de autenticación con OpenAI. Verifica tu clave (OPENAI_API_KEY) y permisos del proyecto/organización.")
    except Exception as e:
        st.warning(f"⚠️ No se pudo detectar el idioma automáticamente: {e}")

    # ── Optional correction helper ────────────────────────────────────────────
    system_msg = None
    if lang == "english":
        system_msg = "You are a helpful English spelling tutor. If there are spelling mistakes in the user's sentence, point them out and show the corrected version. If it is already correct, say 'No spelling issues.'"
    elif lang == "spanish":
        system_msg = "Eres un corrector de español. Si hay errores gramaticales o de ortografía en la oración del usuario, corrígelos y explica brevemente el error. Si todo está bien, di 'Sin errores.'"

    if system_msg:
        try:
            correction = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": user_input},
                ],
                max_tokens=100,
            ).choices[0].message.content.strip()
            if correction.lower() not in {"no spelling issues.", "sin errores."}:
                st.info(f"🔍 **Corrección sugerida:** {correction}")
        except openai.AuthenticationError:
            st.error("❌ Error de autenticación al pedir corrección. Revisa tu clave/API.")
        except Exception as e:
            st.warning(f"⚠️ No se pudo obtener la corrección: {e}")

    # ── Assistant reply (Spanish-only persona kept in system) ─────────────────
    try:
        with st.spinner("Pensando..."):
            response = client.chat.completions.create(
                model=MODEL,
                messages=st.session_state.messages,
                max_tokens=MAX_TOKENS,
            )
        bot_reply = response.choices[0].message.content.strip()
        st.chat_message("assistant").markdown(bot_reply)
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})

        # Cost breakdown (approx)
        pt = getattr(response.usage, "prompt_tokens", 0)
        ct = getattr(response.usage, "completion_tokens", 0)
        total_tokens = (pt or 0) + (ct or 0)
        price = PRICING.get(MODEL, {"input_per_million": 0.0, "output_per_million": 0.0})
        cost = ((pt or 0) / 1_000_000) * price["input_per_million"] + ((ct or 0) / 1_000_000) * price["output_per_million"]
        st.caption(f"🧮 Tokens: {total_tokens} | Cost: ${cost:.8f}")

        st.session_state.rounds += 1

    except openai.AuthenticationError:
        st.error("❌ Error de autenticación con OpenAI durante la respuesta. Asegúrate de que la clave es válida y que tu cuenta tiene acceso al modelo.")
    except Exception as e:
        st.error(f"❌ Error al obtener la respuesta del modelo: {e}")






