import reflex as rx
from ..controllers.user_controllers import get_users, get_user, delete_user
from ..components.add_user_dialog import index as add_user_dialog
import requests

class FormState(rx.State):
    # These track the user input real time for validation
    user_entered_github_username: str = ""
    user_entered_password: str = ""

    # These are the submitted data
    github_username: str = ""
    password: str = ""

    load: bool = False
    isSubmit: bool = False
    user_found: bool = False

    @rx.var
    def github_username_empty(self) -> bool:
        return not self.user_entered_github_username.strip()

    @rx.var
    def password_empty(self) -> bool:
        return not self.user_entered_password.strip()

    @rx.var
    def empty_inputs(self) -> bool:
        return (
            self.github_username_empty or self.password_empty
        )

    def logout(self):
        self.reset()
        self.user_entered_github_username = ""
        self.user_entered_password = ""

    url: str = "https://github.com/reflex-dev"
    profile_image: str = (
        "https://i.sstatic.net/frlIf.png"
    )
    followers: int = 0
    following: int = 0

    def set_profile(self, username: str):
        if username == "":
            return
        github_data = requests.get(
            f"https://api.github.com/users/{username}"
        ).json()
        self.url = github_data["url"]
        self.profile_image = github_data["avatar_url"]
        self.followers = github_data["followers"]
        self.following = github_data["following"]

    def delete_user(self):
        self.user_found = False
        self.load = False
        self.isSubmit = False
        delete_user(self.github_username, self.password)
        self.logout()
        return rx.toast.warning("Usuario eliminado")

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.github_username = form_data.get("github-username")
        self.password = form_data.get("password")

        user = get_user(self.github_username, self.password)

        if len(user) != 0:
            self.user_found = True
            self.load = False
            self.isSubmit = False
            self.set_profile(user[0].github_username)
        else:
            self.user_found = False
            self.load = False
            self.isSubmit = False
            return rx.toast.warning("Usuario o contraseña invalido. Intenta de nuevo")

@rx.page(route='/', title='Inicio de sesión - Osmar')
def index() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.vstack(
                rx.container(
                    rx.container(
                        rx.vstack(
                            rx.container(
                                rx.heading("Acceso", as_="h1", align="center", style={
                                    "font-size": "1.875rem",
                                    "width": "100%",
                                    "color": "#020617",
                                    "margin-bottom": "12px",
                                    "padding": "0"
                                }),
                                rx.vstack(
                                    rx.text(
                                        "Ingrese su usuario de Github a continuación para", align="center", weight="regular",
                                        style={
                                            "font-size": "1rem",
                                            "width": "100%",
                                            "color": "#64748B"
                                        }),
                                    rx.text("Iniciar sesión de cuenta",
                                            align="center", weight="regular",
                                            style={
                                                "font-size": "1rem",
                                                "width": "100%",
                                                "color": "#64748B"
                                            }),
                                    width="100%",
                                    spacing="0"
                                ),
                                style={
                                    "width": "100%",
                                    "margin-bottom": "6px"
                                }
                            ),

                            rx.form.root(
                                rx.vstack(
                                    rx.form.field(
                                        rx.form.label("Nombre de usuario de Github", style={
                                            "color": "#020617"
                                        }),
                                        rx.form.control(
                                            rx.input(
                                                placeholder="Tu nombre de usuario de Github",
                                                name="github-username",
                                                on_change=FormState.set_user_entered_github_username,
                                                type="text",
                                                radius="large",
                                                style={
                                                    "max-width": "32rem",
                                                    "width": "100%",
                                                    "height": "2.25rem"
                                                }
                                            ),
                                            as_child=True,
                                            style={
                                                "width": "100%"
                                            }

                                        ),
                                        rx.cond(
                                            FormState.github_username_empty,
                                            rx.form.message(
                                                "El usuario de Github no puede estar vacío",
                                                color="var(--red-11)",
                                            ),
                                        ),
                                        style={
                                            "width": "100%"
                                        },
                                    ),

                                    rx.form.field(
                                        rx.form.label("Contraseña", style={
                                            "color": "#020617"
                                        }),
                                        rx.form.control(
                                            rx.input(
                                                placeholder="*******",
                                                name="password",
                                                radius="large",
                                                on_change=FormState.set_user_entered_password,
                                                type="password",
                                                style={
                                                    "max-width": "32rem",
                                                    "width": "100%",
                                                    "height": "2.25rem"
                                                }
                                            ),
                                            as_child=True,
                                            style={
                                                "width": "100%"
                                            }
                                        ),

                                        rx.cond(
                                            FormState.password_empty,
                                            rx.form.message(
                                                "La contraseña no puede estar vacío",
                                                color="var(--red-11)",
                                            ),
                                        ),

                                        style={
                                            "width": "100%"
                                        }
                                    ),

                                    rx.form.submit(
                                        rx.button(
                                            "Iniciar sesión",
                                            color_scheme="gray",
                                            type="submit",
                                            radius="large",
                                            on_click=FormState.set_load(True),
                                            loading=FormState.load,
                                            disabled=FormState.empty_inputs,
                                            style={
                                                "width": "100%",
                                                "height": "2.25rem",
                                                "margin-top": "12px"
                                            }
                                        ),
                                        as_child=True,
                                        style={
                                            "width": "100%",
                                            "margin-top": "11px",
                                            "height": "2.5rem",
                                        },
                                    ),
                                    spacing="0"
                                ),
                                on_submit=FormState.handle_submit,
                                reset_on_submit=True
                            ),
                        ),

                        style={
                            "max-width": "100%",
                            "width": "100%",
                        }
                    ),
                    rx.flex(
                        rx.box(
                            rx.vstack(
                                rx.box(
                                    rx.hstack(
                                        rx.avatar(src=FormState.profile_image,
                                                  radius="full", size="3"),
                                        rx.vstack(
                                            rx.vstack(
                                                rx.heading(
                                                    FormState.github_username),
                                                rx.hstack(
                                                    rx.flex(
                                                        rx.link(rx.icon("link", size=16), href=f"https://github.com/{FormState.github_username}", is_external=True)),

                                                    rx.flex(
                                                        rx.icon(
                                                            "users", size=16),
                                                        rx.text(
                                                            FormState.followers),
                                                        align="center"
                                                    ),
                                                    rx.flex(rx.icon("heart", size=10), rx.text(
                                                        FormState.following), align="center"),
                                                    align="center",

                                                ),
                                                spacing="0"
                                            ),

                                            rx.button("Volver a la pantalla de Acceso",
                                                      color_scheme="red", on_click=FormState.logout()),
                                            spacing="2"

                                        ),
                                    )

                                ),
                            
                                rx.alert_dialog.root(
                                    rx.alert_dialog.trigger(
                                        rx.button("Eliminar cuenta?",
                                                  variant="ghost", color_scheme="red", on_click=FormState.delete_user),
                                    ),
                                    rx.alert_dialog.content(
                                        rx.alert_dialog.title("Revoke access"),
                                        rx.alert_dialog.description(
                                            "¿Está seguro? Ya no se podrá acceder a esta aplicación y todas las sesiones existentes expirarán.",
                                            size="2",
                                        ),
                                        rx.flex(
                                            rx.alert_dialog.cancel(
                                                rx.button(
                                                    "Cancelar",
                                                    variant="soft",
                                                    color_scheme="gray",
                                                ),
                                            ),
                                            rx.alert_dialog.action(
                                                rx.button(
                                                    "Eliminar acceso",
                                                    color_scheme="red",
                                                    variant="solid",
                                                ),
                                            ),
                                            spacing="3",
                                            margin_top="16px",
                                            justify="end",
                                        ),
                                        style={"max_width": 450},
                                    ),
                                ),
                                align="center",
                                spacing="5"

                            )
                        ),

                        justify="center",
                        align="center",
                        style={
                            "height": "100%",
                            "width": "100%",
                            "top": "0",
                            "left": "0",
                            "background-color": "white",
                            "position": "absolute",
                            "transform": "translateX(500px)",
                            "transition": ".3s cubic-bezier(1,.09,.19,1.17)",
                            "transform": rx.cond(FormState.user_found, "translateX(0px)", "translateX(500px)")
                        }
                    ),
                    align="center",
                    style={
                        "height": "100%",
                        "width": "100%",
                        "transition": ".3s cubic-bezier(1,.09,.19,1.17)"
                    }
                ),

                style={
                    "width": "480px",
                    "height": "500px",
                    "position": "relative",
                    "overflow": "hidden",
                    "border": "0.1px solid #E4E4E7"
                }

            ),
            rx.vstack(
                add_user_dialog(),
                rx.link(
                    rx.button("Creador por osmarmora05",
                              variant="ghost", color_scheme="gray"),
                    href="https://github.com/osmarmora05",
                    is_external=True
                ),

                justify="center",
                align="center",
            ),

            justify="center",
            align="center",
            spacing="5",
            style={
                "height": "100vh",
                "width": "100%",
            }
        )
    )