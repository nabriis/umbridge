function input_sizes = get_input_sizes(self, config)
if (nargin<2) || (isempty(config))
    config = struct;  % will result in {} in json. Order of fields does not matter
end

% this should only import the functions that we need
import matlab.net.*
import matlab.net.http.*

r = RequestMessage('POST');
value.name = self.model_name;
value.config = config;
r.Body = MessageBody(jsonencode(value));
%disp(r.Body.string);
uri = URI([self.uri,'/InputSizes']);
resp = send(r,uri);
% disp(resp.StatusCode);
% disp(resp.Body.string);
json = jsondecode(resp.Body.string);
input_sizes = json.inputSizes;

end