import pynecone as pc
from webui.components import loading_icon, modal, navbar
from webui.state import State
from webui.styles import *


def message(qa):
    return pc.box(
        pc.box(
            pc.text(
                qa["question"],
                bg=border_color,
                shadow=shadow_light,
                **message_style,
            ),
            text_align="right",
            margin_top="1em",
        ),
        pc.box(
            pc.text(
                qa["answer"],
                bg=accent_color,
                shadow=shadow_light,
                **message_style,
            ),
            text_align="left",
            padding_top="1em",
        ),
        width="100%",
    )


def chat(State):
    return pc.vstack(
        pc.box(pc.foreach(State.chats[State.current_chat], message)),
        py="8",
        flex="1",
        width="100%",
        max_w="3xl",
        padding_x="4",
        align_self="center",
        overflow="hidden",
        padding_bottom="5em",
    )


def action_bar(State):
    return pc.box(
        pc.vstack(
            pc.form(
                pc.form_control(
                    pc.hstack(
                        pc.input(
                            placeholder="Type something...",
                            id="question",
                            _placeholder={"color": "#fffa"},
                            _hover={"border_color": accent_color},
                            style=input_style,
                        ),
                        pc.button(
                            pc.cond(
                                State.processing,
                                loading_icon(height="1em"),
                                pc.text("Send"),
                            ),
                            type_="submit",
                            _hover={"bg": accent_color},
                            style=input_style,
                        ),
                    ),
                    is_disabled=State.processing,
                ),
                on_submit=[State.process_question, pc.set_value("question", "")],
                width="100%",
            ),
            pc.text(
                "PyneconeGPT may return factually incorrect or misleading responses. Use discretion.",
                font_size="xs",
                color="#fff6",
                text_align="center",
            ),
            width="100%",
            max_w="3xl",
            mx="auto",
        ),
        position="sticky",
        bottom="0",
        left="0",
        py="4",
        backdrop_filter="auto",
        backdrop_blur="lg",
        border_top=f"1px solid {border_color}",
        align_items="stretch",
        width="100%",
    )


def navigate_chat(State, chat):
    return pc.hstack(
        pc.box(
            chat,
            on_click=State.set_chat(chat),
            style=sidebar_style,
            color=icon_color,
            flex="1",
        ),
        pc.box(
            pc.icon(
                tag="delete",
                style=icon_style,
                on_click=[State.delete_chat],
            ),
            style=sidebar_style,
        ),
        color=text_light_color,
        cursor="pointer",
    )


def drawer(State):
    return pc.drawer(
        pc.drawer_overlay(
            pc.drawer_content(
                pc.drawer_header(
                    pc.hstack(
                        pc.text("Chats"),
                        pc.icon(
                            tag="close",
                            on_click=State.toggle_drawer,
                            style=icon_style,
                        ),
                    )
                ),
                pc.drawer_body(
                    pc.vstack(
                        pc.foreach(
                            State.chat_title, lambda chat: navigate_chat(State, chat)
                        ),
                        align_items="stretch",
                    )
                ),
            ),
        ),
        placement="left",
        is_open=State.drawer_open,
    )


def index() -> pc.Component:
    return pc.vstack(
        navbar(State),
        chat(State),
        action_bar(State),
        drawer(State),
        modal(State),
        bg=bg_dark_color,
        color=text_light_color,
        min_h="100vh",
        align_items="stretch",
        spacing="0",
    )


# Add state and page to the app.
app = pc.App(state=State, style=base_style)
app.add_page(index)
app.compile()
