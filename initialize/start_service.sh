PORT=2080
CURRENT_DIRECTORY=`pwd`
ENV_DIRECTORY="$(cd ../ && pwd)"/env
LOG_DIRECTORY="$(cd ../ && pwd)"/logs
SRC_DIRECTORY="$(cd ../ && pwd)"/src

# Start ngrok tunnel - Remember to manually close it when finished
"$ENV_DIRECTORY"/ngrok http $PORT >> "$LOG_DIRECTORY"/ngrok.log 2>&1 &
export MYMAC_NGROK_PID=$!

# Update godaddy subdomain
source activate alexa_mymac
python "$CURRENT_DIRECTORY"/update_godaddy_domain.py >> "$LOG_DIRECTORY"/godaddy.log 2>&1

# Start web service
python "$SRC_DIRECTORY"/main.py >> "$LOG_DIRECTORY"/mymac.log 2>&1 &
export MYMAC_WEB_PID=$!
