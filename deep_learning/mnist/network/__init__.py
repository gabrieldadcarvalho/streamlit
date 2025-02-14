def forward(self, x):
  x = self.conv1(x)
  x = self.relu1(x)
  x = self.maxpool1(x)

  x = self.conv2(x)
  x = self.relu2(x)
  x = self.maxpool2(x)

  x = self.flatten(x,1)
  x = self.fc1(x)
  x = self.relu3(x)

  x = self.fc2(x)
  output = self.logSoftmax(x)

  return output