xcopy /Y * C:\Users\Biswjit\Documents\GitHub\FTP /e
cd C:\Users\Biswjit\Documents\GitHub\FTP
git add *
git commit -m "auto_update"
git push origin master
plink.exe Movie_review -l ubuntu -batch /home/ubuntu/web_d.sh

