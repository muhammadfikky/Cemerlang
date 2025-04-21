import streamlit as st
import pandas as pd
import random
import base64
import time

rogers_team = {
    "kurnia",
    "zaenal",
    "guan",
    "alfian",
    "satrio",
    "faisal",
    "najib",
    "roji",
    "fikky",
    "rahmat",
}
voda_team = {
    "wisnu",
    "fikky",
    "roji",
    "rahmat",
    "arsi",
    "alfian",
    "satrio",
    "faisal",
}
att_team = {"kurnia", "zaenal", "roji", "faisal", "satrio"}
sw_team = {"faisal", "endang", "wisnu"}
tr_team = {"yusuf", "enes", "osman"}

all_teams = { 
    "rogers": rogers_team,
    "voda": voda_team,
    "att": att_team,
    "sw": sw_team,
    "tr": tr_team,
}

# SIDEBAR
add_radio = None
with st.sidebar:
    st.title("MAIN MENU")
    with st.expander("Features"):
        add_radio = st.radio("Select a feature", [":material/home_app_logo: Home", ":material/local_fire_department: Skill Detector", 
                                                  ":material/upload: Upload", ":material/build: Tools", ":material/robot_2: Games"])
    with st.expander("Mode"):
        one_piece = """
        ┳┓  •      •       ╻
        ┣┫┏┓┓┏┓┏┓  ┓╋  ┏┓┏┓┃
        ┻┛┛ ┗┛┗┗┫  ┗┗  ┗┛┛┗• 
                ┛          
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⢦⣀⡈⢻⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⡄ ⠙⢿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⢀⣤⣤⣾⣿⠧⠀⠀⠈⢿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠃⠀⠉⠉⠀⠀⠀⠀⢀⣀⣠⣾⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⠇⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⠋⢀⣾⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⢈⠻⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⡇⠀⠸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢦⠈⢿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣷⣾⣿⠃⠀⠀⠀⠀⣸⡄⠀⠀⠀⠀⠘⣷⡀⠻⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⢀⣿⣿⡀⠀⠀⠀⠀⢈⣷⡀⠙⣻⣿⣿⣿
        ⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⢸⣿⣿⣧⠀⠀⠀⠀ ⠘⣿⣾⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿ ⠀⠀  ⣼⣿⣿⣿⣧⠀⠀⠀  ⠈⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⡇  ⠀⠀ ⣿⣿⣿⣿⣿⣿  ⠀  ⠘⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿ ⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠘⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⢻⣿⣿⣿⣿
        ⣿⣿⣿⣿⡏⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠈⣿⣿⣿⣿
        ⣿⣿⣿⡿⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠘⣿⣿⣿
        ⡿⠛⠉⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀ ⠈⠻⣿
        ⣷⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣤⣼
        """
        perf_mode = st.toggle("Performance Mode")
        if perf_mode:
            st.code(one_piece,language=None)

# HOME PAGE
if "Home" in add_radio:
    st.title("Welcome to the IRS Member Hub 🚀")
    st.divider()
    st.subheader("Your all-in-one platform for skill detection, file analysis, tools and also gaming!")
    st.write("Whether you're here to check IRS members skills, analyze files, find a handy tools to make your days easier or even play some fun games, you're in the right place.")
    st.success(":fire: Ready to get started? Pick an option from the sidebar!")
    st.divider()
    
    st.markdown("""
    ### Features Available:
    :material/local_fire_department: :red-background[**Skill Detector**] - Find out which engineers have the skills you’re looking for!  
    :material/upload: :orange-background[**Upload Files**] - Easily upload and explore the contents of your spreadsheet files.      
    :material/build: :blue-background[**Tools**] - To make your work and even life easier! :rocket:                               
    :material/robot_2: :green-background[**Games**] - Play interactive games right inside Streamlit!  
    """)

    st.info(":rocket: Use the sidebar to select a feature and start exploring!")
    st.divider()

    if st.button("Click me!", type="secondary"):
        st.toast("To start..")
        time.sleep(0.5)
        st.toast(":material/west: Go to the sidebar :smile:")
        time.sleep(0.5)
        st.toast(":tada: :tada: :tada:")

# IRS MEMBER SKILL DETECTOR
if "Skill Detector" in add_radio:
    st.title("IRS Member Skill Detector :heart_on_fire:")
    st.divider()
    st.write("Find out our engineers expertise! :rocket: or which engineers have the skills you’re looking for! :sunglasses:")
    st.subheader("Select one:")

    # MENU 1
    menu1 = st.checkbox("Cari nama untuk mendapatkan skills-nya")
    menu2 = st.checkbox("Cari skill untuk mendapatkan nama engineer-nya")
    st.info("Only one option can be selected at a time :material/info:")
    if menu1:
        name = st.text_input("Masukkan nama engineer yang ingin diketahui skills-nya:").lower().strip()
        button1 = st.button("Process Name", type="primary")
        if button1:
            skills = []
            if name in rogers_team:
                skills.append("Rogers")
            if name in voda_team:
                skills.append("Voda")
            if name in att_team:
                skills.append("AT&T")
            if name in sw_team:
                skills.append("SW")
            if name in tr_team:
                skills.append("TR")

            if not name:
                st.write("Sorry, silakan masukkan nama-nya dulu.")
                
            else:
                if skills:
                    nama = name.title()
                    number_of_skill = len(skills) 
                    if number_of_skill == 1:
                        ketiknya = ("skill")
                    elif number_of_skill > 1: 
                        ketiknya = ("skills")
                    if "TR" in skills: 
                        panggilan = "Abi"
                        st.write(f"{nama} {panggilan} memiliki {number_of_skill} {ketiknya} yaitu {' & '.join(skills)}")
                    elif "TR" not in skills: 
                        panggilan = "Abang"
                        if name in ["endang", "kurnia"]:
                            st.write(f"Pak {nama} memiliki {number_of_skill} {ketiknya} yaitu {' & '.join(skills)}")
                        elif name in ["wisnu", "zaenal"]:
                            st.write(f"Om {nama} memiliki {number_of_skill} {ketiknya} yaitu {' & '.join(skills)}")
                        else:
                            st.write(f"{panggilan} {nama} memiliki {number_of_skill} {ketiknya} yaitu {' & '.join(skills)}")

                else:
                    st.write("Sorry, nama yg dimasukkan tdk ada dalam list atau coba cek lg ejaannya.")

    # MENU 2
    # menu2 = st.checkbox("Cari skill untuk mendapatkan nama engineer-nya")
    if menu2:
        which_skills = st.multiselect("Masukkan skills-nya:",["rogers","voda","att","sw","tr"])
        button2 = st.button("Process Skill", type="primary")
        if button2:
            what_and_whose_skills = {} # bikin dictionary baru buat kumpulin skill apa dan siapa nya
            for k, v in all_teams.items(): # loop buat cari apa dan siapa nya dari dict all_teams
                for engineer in v:
                    if engineer in what_and_whose_skills:
                        what_and_whose_skills[engineer].append(k) # looping terus sampe semua kondisi terpenuhi
                    else:
                        what_and_whose_skills[engineer] = [k]  # looping terus sampe semua kondisi terpenuhi
            if not which_skills:
                st.write("Sorry, silakan pilih skill-nya dulu.")
            else:
                found = False # variable found buat cek ada/tidak nya value pas looping
                match = []
                for who, what_skills in what_and_whose_skills.items():
                    if all(skill in what_skills for skill in which_skills): # looping all di dict what_and_whose_skills sampe nemu skill yg sama dgn input dari user
                        match.append(who.title())
                        found = True # kalo gk pake ini error dia

                if found:
                    formatted_skills = []
                    for skill in which_skills:
                        if skill == "att":
                            formatted_skills.append("AT&T")
                        else:
                            formatted_skills.append(skill.title())

                    if "Tr" in formatted_skills:
                        st.write(f"Skill {' & '.join(formatted_skills)} dimiliki oleh:")
                        for who in match:
                            st.write(f"- {who} abi")
                    else:
                        st.write(f"Skill {' & '.join(formatted_skills)} dimiliki oleh:")
                        for who in match:
                            if who in ["Endang", "Kurnia"]: # huruf pertama nya besar karena dia udah diubah di .title() atau bisa jg begini if who.lower() in ["Endang", "Kurnia"]:
                                st.write(f"- Pak {who}")
                            elif who in ["Wisnu", "Zaenal"]: # idem dgn case atasnya ("Pak")
                                st.write(f"- Om {who}")
                            else:
                                st.write(f"- Abang {who}")

                if not found:
                    st.write("Sorry, skills yang anda masukkan tidak ada.")
    
# UPLOAD FILE
if "Upload" in add_radio:
    st.title("Upload Your File :material/upload:")
    st.divider()
    uploaded_file = st.file_uploader("Choose a file:", type=["xlsx", "csv"])
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file)
            elif uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)

            st.success(f"✅ File {uploaded_file.name} uploaded successfully!")
            st.subheader("Data from the file:")
            st.dataframe(df, hide_index=True)
        except Exception as e:
            st.error(f"Error reading the file: {e}")
    else:
        st.info("Please upload a file to view its contents :material/info:")

 
# TOOLS
if "Tools" in add_radio:
    tab1, tab2, tab3 = st.tabs(["Password Generator", "BMI Calculator", "File Merger"])

    with tab1:
        st.header("Welcome to the Password Generator :material/encrypted:")
        st.divider()
        st.write("A new password in seconds :rocket: Built for security & strength! ✅")
        st.write("Give yourself a try :material/encrypted:")
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = st.number_input("How many letters would you like in your password?",min_value=0, max_value=300, placeholder="Type a number...")       
        nr_symbols = st.number_input("How many symbols would you like?",min_value=0, max_value=300, placeholder="Type a number...")
        nr_numbers = st.number_input("How many numbers would you like?",min_value=0, max_value=300, placeholder="Type a number...")

        button = st.button("Generate Password", type="primary")
        st.info("Each parameter has a maximum value of 300. If you require more, please contact me. :material/info:")

        if button:
            random_letters = random.choices(letters, k =nr_letters)
            random_symbols = random.choices(symbols, k =nr_symbols)
            random_numbers = random.choices(numbers, k =nr_numbers)

            random_pswd = random_letters + random_symbols + random_numbers
            random.shuffle(random_pswd)
            final_pswd = "".join(random_pswd)

            st.write("Here is your password:")
            st.write(final_pswd)

    with tab2:
        st.header("Welcome to BMI Calculator :material/vital_signs:")
        st.divider()
        st.write("Know Your Health, Stay in Control! 💪")
        st.write("Give it a go! :material/bolt:")
        st.markdown("Please input your weight in :orange[kilograms] and your height in :orange[meters].")
        weight = st.number_input("Enter your weight:",placeholder="in kilograms...") 
        height = st.number_input("Enter your height:",placeholder="in meters...") 

        button = st.button("Calculate BMI", type="primary")
        if button:
            bmi = weight / (height ** 2)
            if bmi < 18.5:
                st.write("You are underweight :warning: please pay more attention to your health!")
            elif bmi < 25:
                st.write("You have normal weight ✅ keep up the good work! :sunglasses:")
            elif bmi < 30 :
                st.write("You are overweight :warning: please pay more attention to your health!")
            else:
                st.write("You are obese! 🛑 you need to be aware and pay close attention to your health.")

    with tab3:
        import io
        from datetime import datetime
        st.header("Welcome to File Merger Tools!")
        st.divider()
        st.write("Upload, Merge, Download! :rocket:")
        st.write("No complicated formulas, no manual copy-pasting! :no_entry:")
        st.write("Seamless and effortless :sunglasses:")
        st.info("For now it only support xlxs and csv only. :material/info:")

        uploaded_files = st.file_uploader("Upload Excel or CSV Files", type=["xlsx", "csv"], accept_multiple_files=True)

        if "merged_file" not in st.session_state:
            st.session_state.merged_file = None
        if "output_filename" not in st.session_state:
            st.session_state.output_filename = None

        if uploaded_files:
            if len(uploaded_files) < 2:
                st.warning("⚠️ Please upload at least **two files** to proceed.")
            else:
                st.write("📂 Uploaded Files:")
                for file in uploaded_files:
                    st.write(f"✅ {file.name}")
                st.info("Please make sure you uploaded the correct files.")

                if st.button("Process",type="primary"):
                    merged_sheets ={}
                    progress_text = st.empty()

                    progress_bar = st.progress(0)
                    total_files = len(uploaded_files)

                    for i, file in enumerate(uploaded_files):
                        if file.name.endswith(".xlsx"):
                            sheets = pd.read_excel(file, sheet_name=None)
                            for sheet_name, df in sheets.items():
                                merged_sheets.setdefault(sheet_name, pd.DataFrame())
                                merged_sheets[sheet_name] = pd.concat([merged_sheets[sheet_name], df], ignore_index=True)

                        elif file.name.endswith(".csv"):
                            df = pd.read_csv(file)
                            sheet_name = file.name.replace(".csv", "")
                            merged_sheets.setdefault(sheet_name, pd.DataFrame())
                            merged_sheets[sheet_name] = pd.concat([merged_sheets[sheet_name], df], ignore_index=True)
                        
                        percentage = ((i + 1) / total_files) * 100
                        progress_bar.progress((i + 1) / total_files)
                        progress_text.text(f"Progress: {int(percentage)}% completed")

                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine="openpyxl") as writer:
                        for sheet_name, df in merged_sheets.items():
                            df.to_excel(writer, sheet_name=sheet_name, index=False)

                    output.seek(0)
                    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
                    st.session_state.output_filename = f"Merged_Data_{current_time}.xlsx"
                    st.session_state.merged_file = output

            if st.session_state.merged_file and st.session_state.output_filename:
                st.success("Done! Your file is ready for download.")
                if st.download_button(label="Download",type="primary",
                                    data=st.session_state.merged_file,
                                    file_name=st.session_state.output_filename,
                                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"):
                    st.markdown(":orange[It is always good to double check. Tools are meant to help you, not to replace you!] :warning:")

# GAMES
if "Games" in add_radio:
    tab1, tab2 = st.tabs(["Rock Paper Scissors", "Treasure Island"])
    with tab1:
        st.title("Welcome to Rock Paper Scissors Game!")
        st.divider()
        st.write("Who Wins? Let’s Find Out! :fire:")
        on = st.toggle("Hint.")
        if on:
            st.caption("0 for Rock :material/weight:")
            st.caption("1 for Paper :material/description:")
            st.caption("2 for Scissors :material/content_cut:")

        rock = ("""Rock
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)

        paper = ("""Paper
            _______
        ---'    ____)____
                    ______)
                   _______)
                  _______)
        ---.__________)
        """)

        scissors = ("""Scissors
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

        game_images = [rock, paper, scissors]

        choose = st.number_input("What do you choose?",min_value=0, max_value=2, placeholder="Type a number between 0 - 2")
        button = st.button("Play", type="primary")
        if button:
            if choose >=0 and choose <=2:
                st.write(":material/person: You chose:")
                st.code(game_images[choose],language=None)

            game = random.randint(0,2)
            st.write(":material/robot_2: Computer chose:")
            st.code(game_images[game], language=None)

            if choose == game:
                st.write("It's a draw! :handshake:")
            if choose == 1 and game == 0:
                st.write("You win! :tada:")
            if choose == 2 and game == 0:
                st.write("You lose! :disappointed:")
            if choose == 0 and game == 1:
                st.write("You lose! :disappointed:")
            if choose == 2 and game == 1:
                st.write("You win! :tada:")
            if choose == 0 and game == 2:
                st.write("You win! :tada:")
            if choose == 1 and game == 2:
                st.write("You lose! :disappointed:")

            st.markdown("🔄 Play Again? :gray[*Because one round is never enough!*]")


            # if st.button("🔄 Play Again"):
            #     st.experimental_user()

    with tab2:
        st.title("Welcome to Treasure Island! :coin:")
        st.markdown("Your mission is to find the :orange[treasure] :sunglasses:")
        st.code('''             *******************************************************************************
                  |                   |                  |                     |
        __________|________________.=""_;=.______________|_____________________|_______
        |                   |  ,-"_,=""     `"=.|                  |
        |___________________|__"=._o`"-._        `"=.______________|___________________
                  |                `"=._o`"=._      _`"=._                     |
        __________|_____________________:=._o "=._."_.-="'"=.__________________|_______
        |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
        |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                  |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
        __________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
        |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
        |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
        ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
        /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
        ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
        /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
        ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
        /______/______/______/______/______/______/______/______/______/______/_______/
        *******************************************************************************''')
        st.divider()
        st.success(":fire: Let's get started!")
        st.write("You are at the cross road. Where do you want to go?")
        option1 = ["Right", "Left"]
        selection1 = st.pills("What is your choice?", option1, selection_mode="single")
        if selection1 == "Left":
            st.write("You've come to a lake. There is an island in the middle of the lake.")
            option2 = ["Wait", "Swim"]
            selection2 = st.pills("What is your choice? Wait for a boat or swim to swim accross", option2, selection_mode="single")
            if selection2 == "Wait":
                st.write("You arrive at the island unharmed. There is house with 3 doors. One red, one yellow and one blue. Which colour will you choose?")
                option3 = ["Red", "Yellow", "Blue"]
                selection3 = st.pills("What is your choice?", option3, selection_mode="single")
                if selection3 == "Yellow":
                    st.code(r"""
                                                                                _.--. 
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
               '-._'-.|| |' `_.-'
                    '-.||_/.-""")
                    st.markdown("You found the treasure 🤩 You :orange[win]! Congratulations! :tada:")
                
                elif selection3 == "Red":
                    st.markdown("It's a room full of :orange[fire]! :fire: :sob: Game Over.")
                elif selection3 == "Blue":
                    st.markdown("You enter a room of beasts! 😵‍💫 Game Over.")
            elif selection2 == "Swim":
                st.markdown("You got attacked by an angry trout! :sob: Game Over.")
        elif selection1 == "Right":
            st.markdown("You fell in to a hole! :sob: Game Over.")

        




