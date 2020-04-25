# Passphrase

A Python library for generating passphrases with numbers and special characters.


## Why use this script?

By now it is generally accepted fact that passphrases are more effective then traditionnal complex passwords and also a lot easier to type and remember.

For reference, here is an extract from the SANS institute article: [OUCH!  April 2017 Passphrases](https://www.sans.org/security-awareness-training/ouch-newsletter/2017/passphrases)
> The challenge we all face is that cyber attackers have developed sophisticated and effective methods to brute force (automated guessing) passwords. This means bad guys can compromise your passwords if they are weak or easy to guess. An important step to protecting yourself is to use strong passwords. Typically, this is done by creating complex passwords; however, these can be hard to remember, confusing, and difficult to type. Instead, we recommend you use passphrases--a series of random words or a sentence. The more characters your passphrase has, the stronger it is.  The advantage is these are much easier to remember and type, but still hard for cyber attackers to hack.

There are now several websites offering the ability to generate cryptographically strong passphrases, such as the [Diceware Eff wordlist](https://www.rempe.us/diceware/#eff).
> Diceware is used to generate cryptographically strong passphrases. Don't let that frighten you away though, a passphrase is just a password made of words you can remember. It is based on the principle that truly random selection of words from a wordlist, can result in easily memorable passwords that are also extremely resistant to attack. Traditional Diceware uses rolls of physical dice, this application uses a strong random number generator in place of the dice. Passwords that are six words or longer are thought to be safe for any very high security applications.

However, being able to generate such passphrases locally on your system without having to use a third-party website might be preferable.


## Installation

Download or clone this repository, cd to the directory.

The dictionary words used in this example are from [google-10000-english-usa-no-swears-long](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears-long.txt), please review their [licensing terms](https://github.com/first20hours/google-10000-english/blob/master/LICENSE.md) before use and replace the content of the `american-english` file with your own words before installing if needed.

Obviously if everyone uses the same list then the random aspect of this script will greatly be diminished.


To install:

```
python3 setup.py install
```


## usage

This script is used to generate a passphrase of between 2 to 5 dictionary words with random first letter
capitalization and a random number of special characters between the words.


```
passphrase
30iconic(0-$0*0Glow*-Valved-begrudge
```

## Windows Download
Also available as a [Windows executable download](https://github.com/Videre-Research-LLC/python-passphrase/releases/tag/v1.0)
