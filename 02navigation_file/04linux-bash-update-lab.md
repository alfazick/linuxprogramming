# Customizing Linux: The Dotfile Movement

## Introduction to Dotfiles

The default console in Linux isn't always user-friendly. Since there are no graphical interfaces for many settings, people have started experimenting with the appearance and functionality of the console through text-based configurations.

If you've seen cool-looking terminals in videos or movies, chances are they've been customized using dotfiles. Dotfiles are configuration files that start with a dot (.) and are used to personalize your system.

## The Dotfile Community

Luckily for us, many enthusiasts share their dotfiles publicly. Here are some popular dotfile repositories:

- [Mathias Bynens](https://github.com/mathiasbynens/dotfiles)
- [Zach Holman](https://github.com/holman/dotfiles)
- [Nick Nisi](https://github.com/nicknisi/dotfiles)
- [Webpro's Dotfiles for macOS](https://github.com/webpro/dotfiles)
- [Dotfiles GitHub Community](https://github.com/webpro/awesome-dotfiles)
- [Jess Fraz](https://github.com/jessfraz/dotfiles)

## Customizing Your Bash Prompt

We'll use Jess Fraz's `.bash_prompt` as an example to customize our bash prompt. This script includes several advanced features:

1. Setting $TERM based on terminal capabilities
2. Git prompt customization
3. Cloud environment detection
4. Color customization
5. Prompt customization (PS1)
6. Secondary prompt customization (PS2)

### Steps to Customize Your Prompt

1. Download the bash prompt script:
   ```
   curl https://raw.githubusercontent.com/jessfraz/dotfiles/master/.bash_prompt > bash_experiment.txt
   ```

2. Backup your existing .bashrc:
   ```
   cp ~/.bashrc ~/.bashrc.backup
   ```

3. Open your .bashrc file in a text editor:
   ```
   nano ~/.bashrc
   ```

4. Append the contents of bash_experiment.txt to your .bashrc. You can do this by copying and pasting, or by using this command:
   ```
   cat bash_experiment.txt >> ~/.bashrc
   ```

5. Test the changes by opening a new terminal or sourcing your .bashrc:
   ```
   source ~/.bashrc
   ```

6. Personalize: Feel free to modify any part of the script to suit your preferences.

### Assignment: Add Time to Your Prompt

To add the current time to your prompt, add these lines to the end of your .bashrc:

```bash
get_current_time() {
    echo $(date +"%d-%m-%Y %H:%M:%S")
}
PS1+="\\[$white\\][\$(get_current_time)] ";
```

This will add the current date and time to your prompt.

## Tips for Customization

1. Always backup your configuration files before making changes.
2. Test changes in a new terminal window before making them permanent.
3. Read through the scripts you're adding to understand what they do.
4. Don't be afraid to experiment and make changes to suit your needs.
5. Remember that customization is about making your environment work best for you.

By following these steps, you'll have a highly customized and informative bash prompt. As you become more comfortable with dotfiles, you can explore other customizations to further enhance your Linux experience.

