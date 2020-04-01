import win32com.client as win32

search_str = 'Error requesting data'

outlook = win32.Dispatch('outlook.application')
namespace = outlook.GetNamespace('MAPI')
# get unread emails from service alerts folder, in my outlook it's folder 0 of the main inbox
svc_alerts = namespace.Folders['example@example.com'].Folders['Inbox'].Folders[0].Items.Restrict('[Unread] = true')

count = 0
to_delete = []

# split finding and deleting into two loops - deleting as you go shortens
# the list and you only go through half of the total emails
print('Finding emails to delete')
for alert in svc_alerts:
	body = alert.Body
	if search_str in body:
		to_delete.append(alert)

print('Deleting ' + len(to_delete) + ' emails')
for alert in to_delete:
	alert.delete()
	count += 1
	if count % 1000 == 0:
		print('Deleted ' + str(count) + '...')

print('Finished. Deleted ' + str(count))
