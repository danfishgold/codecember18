module Markup exposing (Day, document, parseDocument)

import Element exposing (Element)
import Element.Font as Font
import Mark exposing (Record)
import Mark.Error as Error exposing (Error)


type alias Day msg =
    { day : Int
    , title : String
    , images : List Image
    , description : Element msg
    }


type alias Image =
    String


parseDocument : String -> Result (List Error) (List (Day msg))
parseDocument string =
    case Mark.compile document string of
        Mark.Success days ->
            Ok days

        Mark.Failure errors ->
            Err errors

        Mark.Almost { errors } ->
            Err errors


errorsElement : List Error -> Element msg
errorsElement errors =
    case errors of
        firstError :: _ ->
            Element.html (Error.toHtml Error.Light firstError)

        [] ->
            Element.text "ERRORS BUT NO ERRORS???"


document : Mark.Document (List (Day msg))
document =
    Mark.document identity <|
        Mark.manyOf [ dayBlock ]


dayBlock : Mark.Block (Day msg)
dayBlock =
    Mark.record "Day"
        Day
        |> Mark.field "day" Mark.int
        |> Mark.field "name" Mark.string
        |> Mark.field "images" (Mark.manyOf [ image ])
        |> Mark.field "description" descriptionBlock
        |> Mark.toBlock


image : Mark.Block Image
image =
    Mark.block "Image"
        identity
        Mark.string


descriptionBlock : Mark.Block (Element msg)
descriptionBlock =
    Mark.textWith
        { view = styleText
        , inlines = [ link ]
        , replacements = Mark.commonReplacements
        }
        |> Mark.map (\texts -> Element.paragraph [] texts)


link : Record (Element msg)
link =
    Mark.annotation "link"
        (\styles url ->
            Element.link [ Font.underline ]
                { url = url
                , label = styleLink styles
                }
        )
        |> Mark.field "url" Mark.string


styleLink : List ( Mark.Styles, String ) -> Element msg
styleLink tuples =
    -- Element.wrappedRow [] (List.map (\( styles, string ) -> styleText styles string) tuples)
    tuples |> List.map Tuple.second |> String.join "" |> Element.text


styleText : Mark.Styles -> String -> Element msg
styleText { bold, italic, strike } string =
    if bold || italic || strike then
        Element.el
            (List.filterMap identity
                [ if bold then
                    Just Font.bold

                  else
                    Nothing
                , if italic then
                    Just Font.italic

                  else
                    Nothing
                , if strike then
                    Just Font.strike

                  else
                    Nothing
                ]
            )
            (Element.text string)

    else
        Element.text string