import hashlib
import os
import random
import string
from time import sleep
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

common_words = ["password", "123456", "admin", "letmein", "welcome", "qwerty", "monzurul", "akash", "secret", "test"]

def banner():
    console.print(Panel.fit("[bold cyan]🔐 HASH ENCRYPT-DECRYPT TOOL 🔐[/bold cyan]\n[green]By Monzurul | Supports MD5, SHA, etc.\nWorks on Windows, Linux, Termux", title="Welcome", border_style="cyan"))

def encrypt_string(text):
    console.print("\n[bold yellow]🔒 Encrypted Hashes:[/bold yellow]")
    hashes = {
        "MD5": hashlib.md5(text.encode()).hexdigest(),
        "SHA1": hashlib.sha1(text.encode()).hexdigest(),
        "SHA256": hashlib.sha256(text.encode()).hexdigest(),
        "SHA512": hashlib.sha512(text.encode()).hexdigest(),
    }
    for name, value in hashes.items():
        console.print(f"[blue]{name}:[/blue] [white]{value}[/white]")
    save = Prompt.ask("\nDo you want to save these to a file? (y/n)", default="n")
    if save.lower() == "y":
        with open("hash_output.txt", "w") as f:
            for name, value in hashes.items():
                f.write(f"{name}: {value}\n")
        console.print("[green]Saved to hash_output.txt[/green]")

def decrypt_hash(hash_input):
    console.print("\n[bold red]🔓 Trying to Decrypt...[/bold red]")
    sleep(1)
    for word in common_words:
        if hashlib.md5(word.encode()).hexdigest() == hash_input:
            console.print(f"[green]Matched MD5[/green]: {word}")
            return
        elif hashlib.sha1(word.encode()).hexdigest() == hash_input:
            console.print(f"[green]Matched SHA1[/green]: {word}")
            return
        elif hashlib.sha256(word.encode()).hexdigest() == hash_input:
            console.print(f"[green]Matched SHA256[/green]: {word}")
            return
        elif hashlib.sha512(word.encode()).hexdigest() == hash_input:
            console.print(f"[green]Matched SHA512[/green]: {word}")
            return
    console.print("[red]No match found using dictionary method.[/red]")

def generate_password():
    console.print("\n[bold magenta]🔑 Secure Password Generator[/bold magenta]")
    length = int(Prompt.ask("Enter password length", default="12"))
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    console.print(f"[bold green]Generated Password:[/bold green] {password}")

def main_menu():
    banner()
    while True:
        console.print("\n[bold cyan]Menu:[/bold cyan]")
        console.print("[1] Encrypt Text")
        console.print("[2] Try to Decrypt Hash")
        console.print("[3] Generate Password")
        console.print("[4] Exit")
        choice = Prompt.ask("Choose an option", default="1")

        if choice == "1":
            user_text = Prompt.ask("Enter text to encrypt")
            encrypt_string(user_text)
        elif choice == "2":
            user_hash = Prompt.ask("Enter hash to decrypt")
            decrypt_hash(user_hash.strip().lower())
        elif choice == "3":
            generate_password()
        elif choice == "4":
            console.print("[bold red]Exiting...[/bold red] 🔐")
            break
        else:
            console.print("[red]Invalid choice![/red]")

if __name__ == "__main__":
    main_menu()
