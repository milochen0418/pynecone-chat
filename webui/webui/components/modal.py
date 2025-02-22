import pynecone as pc


def modal(State):
    return pc.modal(
        pc.modal_overlay(
            pc.modal_content(
                pc.modal_header(
                    pc.hstack(
                        pc.text("Create new chat"),
                        pc.icon(
                            tag="close",
                            font_size="sm",
                            on_click=State.toggle_modal,
                            color="#fff8",
                            _hover={"color": "#fff"},
                            cursor="pointer",
                        ),
                        align_items="center",
                        justify_content="space-between",
                    )
                ),
                pc.modal_body(
                    pc.input(
                        placeholder="Type something...",
                        on_blur=State.set_new_chat_name,
                        bg="#222",
                        border_color="#fff3",
                        _placeholder={"color": "#fffa"},
                    ),
                ),
                pc.modal_footer(
                    pc.button(
                        "Create",
                        bg="#5535d4",
                        box_shadow="md",
                        px="4",
                        py="2",
                        h="auto",
                        _hover={"bg": "#4c2db3"},
                        on_click=[State.create_chat, State.toggle_modal],
                    ),
                ),
                bg="#222",
                color="#fff",
            ),
        ),
        is_open=State.modal_open,
    )
