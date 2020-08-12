# Add-comment_workitem
# For manuall run
main.py --buildid "$(Build.BuildId)" --comment "$(MyComment)" --token "$(System.AccessToken)" --org "https://dev.azure.com/arxspan" --proj "Biology Editor"

# Azure pipeline example
- task: PythonScript@0
        inputs:
          # scriptSource: 'filePath' # Options: filePath, inline
          scriptPath: $(Build.Repository.LocalPath)/ops-tools/az-scripts/scrape_items/main.py  
          #script: # Required when scriptSource == inline
          arguments: '--buildid "$(Build.BuildId)" --comment "$(MyComment)" --token "$(System.AccessToken)" --org "https://dev.azure.com/arxspan" --proj "Biology Editor"'
          # pythonInterpreter: '$(python.version)' # Optional
          #workingDirectory: # Optional
          #failOnStderr: false # Optional
