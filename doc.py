import paramiko
import time


def clone_repo_init_and_export_key_on_ec2(instance_ip, instance_username, instance_private_key_path, repo_directory, repo_url, openai_api_key, repo_name):
    # Create an SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    try:
        # Connect to the EC2 instance
        ssh_client.connect(
            hostname=instance_ip,
            username=instance_username,
            key_filename=instance_private_key_path
        )


        # Start an interactive shell session
        shell = ssh_client.invoke_shell()
        shell.send(f'git clone {repo_url}\n')
        time.sleep(1)
        # Change to the repository directory
        shell.send(f'cd {repo_directory}\n')
        time.sleep(1)


        # Export the OpenAI API key as an environment variable
        shell.send(f'echo "export OPENAI_API_KEY=\\"{openai_api_key}\\"" >> ~/.bashrc\n')
        time.sleep(1)


        # Run the 'doc init' command inside the repository directory
        shell.send('doc init\n')
        time.sleep(5)


        # Automatically answer the prompts by sending the repository name, URL, and pressing Enter
        shell.send(f'{repo_name}\n')
        time.sleep(5)
        shell.send(f'{repo_url}\n')
        time.sleep(5)
        shell.send('\n')
        time.sleep(5)


        # Wait for the command execution to complete


        # Create a text file named sineth.txt
        shell.send('doc index\n')
       


        # Wait for the command execution to complete
        time.sleep(10)


        shell.send('Y\n')
        time.sleep(60)






        # Close the shell session
        shell.close()


    finally:
        # Close the SSH connection
        ssh_client.close()




# Example usage
instance_ip = 'ec2-3-144-83-37.us-east-2.compute.amazonaws.com'
instance_username = 'ec2-user'
instance_private_key_path = 'C:/Users/Sineth/Desktop/newdoc23.pem'
repo_directory = 'software-industry-competitor'
repo_url = 'https://github.com/tahakhawaja/software-industry-competitor.git'
openai_api_key = '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'
repo_name = 'software-industry-competitor'


clone_repo_init_and_export_key_on_ec2(instance_ip, instance_username, instance_private_key_path, repo_directory, repo_url, openai_api_key, repo_name)
