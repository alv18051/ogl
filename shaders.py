vertex_shader ='''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;


out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    
    UVs = texcoords;
    norms = normals;
    pos = (modelMatrix * vec4(position, 1.0)).xyz;


    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);
}
'''

fragment_shader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D texture0;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    fragColor = texture(texture0, UVs) * intensity;
}
'''
toon_vertex_shader = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;
out vec3 outColor;
out vec2 outTexCoords;
void main()
{
    vec4 norm = vec4(normal, 0.0);
    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;
    vec4 light = vec4(pointLight, 1.0);
    float intensity = dot(modelMatrix * norm, normalize(light - pos));
    
    intensity = intensity + 0.3;
    if (intensity >= 1) {
        intensity = 1;
    }
    if (intensity >= 0.8) {
        intensity = 1;
    }
    else if (intensity >= 0.5) {
        intensity = 0.6;
    }
    else if (intensity >= 0.2) {
        intensity = 0.4;
    }
    else if (intensity >= 0.1) {
        intensity = 0.3;
    }
    else {
        intensity=0.1;
    }
    gl_Position = projectionMatrix * viewMatrix * pos;
    outColor = vec3(1.0,1.0 - valor * 2,1.0-valor * 2) * intensity;
    outTexCoords = texCoords;
}
"""

toon_fragment_shader = """
#version 450
layout (location = 0) out vec4 fragColor;
in vec3 outColor;
in vec2 outTexCoords;
uniform sampler2D tex;
void main()
{
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords);
}
"""
