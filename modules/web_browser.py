import webbrowser as wb

done = False

while not done:
    print("O que vocẽ deseja fazer? ")
    print("Ver meu portfólio no github? Digite 1")
    print("Ver meu perfil do linkedin? Digite 2")
    print("Falar comigo via Whatsapp? Digite 3")
    print("Sair? Digite 4")

    choice = input(">")

    if choice == "1":
        wb.open('https://github.com/robertomoreira04')
    elif choice == "2":
        wb.open('https://www.linkedin.com/in/roberto-m-3b6ba3290/')
    elif choice == "3":
        wb.open('https://wa.me/5584996277529')
    elif choice == "4":
        print("Obrigado, até mais!")
        done = True
    else:
        print("Opção inválida. Escolha um número entre 1 a 4.")

