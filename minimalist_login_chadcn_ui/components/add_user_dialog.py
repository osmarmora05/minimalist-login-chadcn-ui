import reflex as rx
import requests
from ..controllers.user_controllers import get_username, create_user
from ..utils.encrypt import password_encrypt, decrypt_password

class AlertDialogState(rx.State):
    new_user_entered_github_username: str = ""
    new_user_entered_password: str = ""
    new_user_confirm_entered_password: str = ""

    new_github_username: str = ""
    new_password: str = ""

    load: bool = False
    isOpen: bool = False

    @rx.var
    def new_github_username_empty(self) -> bool:
        return not self.new_user_entered_github_username.strip()

    @rx.var
    def new_password_empty(self) -> bool:
        return not self.new_user_entered_password.strip()

    @rx.var
    def new_user_confirm_entered_password_empty(self) -> bool:
        return not self.new_user_confirm_entered_password.strip()

    @rx.var
    def password_is_equal(self) -> bool:
        if not self.new_password_empty and not self.new_user_confirm_entered_password_empty:
            if self.new_user_entered_password == self.new_user_confirm_entered_password:
                return True
            else:
                return False

    @rx.var
    def empty_inputs(self) -> bool:
        return (
            self.new_github_username_empty or not self.password_is_equal
        )

    def reset_values(self):
        self.new_user_entered_github_username = ""
        self.new_user_entered_password = ""
        self.new_github_username: str = ""
        self.new_user_confirm_entered_password = ""
        self.load = False
        self.isOpen = False

    def close_dialog(self, value: bool):
        if value == True:
            self.reset_values()
            self.isOpen = value

    def handle_submit(self):
        self.new_github_username = self.new_user_entered_github_username
        self.new_password = self.new_user_entered_password
        self.load = True
        self.isOpen = True

        github_data = requests.get(
            f"https://api.github.com/users/{self.new_github_username}"
        ).json()
        

        if github_data.get('status') == "404" or github_data.get('status') is not None:
            self.load = False
            return rx.toast.warning("Oye! Ingresa un usuario de github valido")

        user = get_username(self.new_github_username)
        is_user = False
        for x in user:
            if (self.new_password == decrypt_password(x.password)):
                is_user = True

        if is_user:
            self.load = False
            return rx.toast.warning("Parace que ya existe la cuenta :v")
        

        encrypted_password = password_encrypt(self.new_password)
        create_user(self.new_github_username, encrypted_password)
        self.isOpen = False
        return rx.toast.success("Genial! cuenta creada")


def index() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("Crear cuenta",
                          variant="ghost", color_scheme="green")),
        rx.dialog.content(
            rx.dialog.title("Registrar Cuenta"),
            rx.dialog.description(
                "Llena tus datos",
                size="2",
                margin_bottom="16px",
            ),
            rx.flex(
                rx.box(
                    rx.text(
                        "Nombre de usuario de Github",
                        as_="div",
                        size="2",
                        margin_bottom="4px",
                        weight="bold",
                    ),
                    rx.input(
                        placeholder="Tu nombre de usuario de Github",
                        radius="large",
                        on_change=AlertDialogState.set_new_user_entered_github_username,
                        style={
                            "height": "2.25rem",
                            "margin-bottom": "4px"
                        }

                    ),
                    rx.cond(
                        AlertDialogState.new_github_username_empty,
                        rx.text("El usuario de Github no puede estar vacío",
                                color="var(--red-11)", size="1")
                    )
                ),
                rx.box(
                    rx.text(
                        "Contraseña",
                        as_="div",
                        size="2",
                        margin_bottom="4px",
                        weight="bold",
                    ),
                    rx.input(
                        placeholder="*******",
                        on_change=AlertDialogState.set_new_user_entered_password,
                        type="password"
                    ),
                    rx.cond(
                        AlertDialogState.new_password_empty,
                        rx.text("La contraseña no puede estar vacío",
                                color="var(--red-11)", size="1")
                    )
                ),

                rx.box(
                    rx.text(
                        "Confirmar contraseña",
                        as_="div",
                        size="2",
                        margin_bottom="4px",
                        weight="bold",
                    ),
                    rx.input(
                        placeholder="*******",
                        on_change=AlertDialogState.set_new_user_confirm_entered_password,
                        type="password"
                    ),

                    rx.cond(
                        AlertDialogState.new_user_confirm_entered_password_empty,
                        rx.text("La contraseña no puede estar vacío",
                                color="var(--red-11)", size="1")
                    )
                ),

                rx.separator(),
                rx.cond(
                    AlertDialogState.password_is_equal,
                    rx.text("Contraseñas iguales",
                            color="var(--green-11)", size="1"),
                    rx.text("Contraseñas no coinciden", size="1",
                            color="var(--red-11)")
                ),

                direction="column",
                spacing="3",
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        "Cancelar",
                        color_scheme="gray",
                        variant="soft",
                        on_click=AlertDialogState.reset_values
                    ),
                ),
                rx.dialog.close(
                    rx.button("Guardar", color_scheme="gray",
                              radius="large", disabled=AlertDialogState.empty_inputs, on_click=AlertDialogState.handle_submit, loading=AlertDialogState.load),
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
        ),
        on_open_change=AlertDialogState.close_dialog,
        open=AlertDialogState.isOpen
    )