echo "Enter commit message:"
read message

git add
git commit -m "$message"
git push
chromium "https://www.pythonanywhere.com/user/tobiasrestapi/consoles/34512460/"