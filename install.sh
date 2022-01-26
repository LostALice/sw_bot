now=$(date +"%s")

docker image build -t sw_bot:$now .

echo -e "\e[1;35m Build successfully \e[0m"