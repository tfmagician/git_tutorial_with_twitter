require_recipe "python"

python_pip "flask" do
    action :install
    version "0.8"
end

python_pip "tweepy" do
    action :install
    version "1.4"
end
