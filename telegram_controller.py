import telepot
import money_operation_service
import time

money_operation_service.topup(
    user_id='rizkirank',
    topup_amount=50000
)
money_operation_service.print_stats()
bot = None

def set_bot(bot_kita):
    global bot
    bot = bot_kita

def handle_transfer(*args, **kwargs):
    source_id = kwargs['source_id']
    send_amount = kwargs['send_amount']
    destination_id = kwargs['destination_id']
    money_operation_service.send(
        source_user_id=source_id,
        send_amount=send_amount,
        destination_user_id=destination_id
    )
    money_operation_service.print_stats()
    return 'Uang anda yang tersisa: %d'  % money_operation_service.retrieve_amount(user_id=source_id)


def handle(msg):
    source_id = msg['from']['username']
    source_number = msg['from']['id']
    command = msg['text'].split(' ')
    if command[0] == 'kirim':
        destination_id = command[1]
        send_amount = int(command[2])
        response = handle_transfer(
            source_id=source_id,
            send_amount=send_amount,
            destination_id=destination_id)
        bot.sendMessage(source_number, response)

